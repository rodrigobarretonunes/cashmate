from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import UserCreate
from models import User

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



    


