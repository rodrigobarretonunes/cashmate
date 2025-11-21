from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends, Request
from models import User
from datetime import datetime, timezone, timedelta
from passlib.context import CryptContext
import os 
import dotenv
from schemas import TokenResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from fastapi.security import OAuth2PasswordBearer



dotenv.load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Password hashing context
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Function to hash a password
def get_password_hash(password: str):
    hashed_password = pwd_context.hash(password)
    return hashed_password


# Function to verify a password
def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)


# Function to create access token
def create_access_token(db_user: User):
    try:
        to_encode = {
            "sub": str(db_user.id), 
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email
        }
        expire = datetime.now(timezone.utc) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
    
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt  
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating access token: " + str(e))
    
def token_validation(request):
    token = request.headers.get("Authorization")
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticação não fornecido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if token.startswith("Bearer "):
        token = token[7:]
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
        )
    

def get_current_user(request:Request, db:Session):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    try:
        token_type,token = auth_header.split(" ")
        if token_type.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid token type")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        stmt = select(User).where(User.id == user_id)
        user = db.execute(stmt).scalars().first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Token decode error")


