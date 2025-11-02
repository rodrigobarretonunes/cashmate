from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import UserCreate, UserLogin, TokenResponse
from models import User
from fastapi import HTTPException
from jwt import encode, decode
import os 
import dotenv
from datetime import datetime,timedelta, timezone


dotenv.load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


# Password hashing context
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Function to hash a password
def get_password_hash(password: str):
    hashed_password = pwd_context.hash(password)
    return hashed_password

# Function to verify a password
def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)

# Function to register a new user
async def create_user(db:Session, user:UserCreate, hashed_password:str):
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Function to verify if a user already exists
def verify_if_user_exists(db: Session, username: str):
    stmt = select(User).where(User.username == username)
    return db.execute(stmt).scalars().first()

async def login_user(db: Session, user:UserLogin):
    try:
        db_user = authenticate_user(db,user)
        if not db_user:
            raise HTTPException(status_code=400, detail='Invalid credentials, (login_user)')
        token = create_access_token(db_user)
        print(f"Token created successfully,{token}")
        return token
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    



#Function to validate user
def authenticate_user(db: Session, user:UserLogin):
    try:
        stmt = select(User).where(User.username == user.username)
        db_user = db.execute(stmt).scalars().first()
        if not db_user.username:
            raise HTTPException(status_code=400, detail="Invalid username, (authenticate_user)")
        if not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(status_code=400, detail="Invalid password, (authenticate_user)")
        return db_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Function to create access token
def create_access_token(db_user:User): # Data have some user infos like: id, username,email
    try:
        to_encode = {
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email
        }
        expire = datetime.now(timezone.utc) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp":expire})
        encoded_jwt = encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
        return TokenResponse(access_token=encoded_jwt)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating access token:" + str(e))
    
    









    


