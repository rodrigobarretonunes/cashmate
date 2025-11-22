
from sqlalchemy.orm import Session
from sqlalchemy import select
from .auth_schemas import UserCreate, UserLogin
from .auth_models import User
from core import verify_password,create_access_token
from fastapi import HTTPException


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
        token = create_access_token(user_id=db_user.id,username=db_user.username,email=db_user.email)
        return token
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# Function to validate user
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
    


