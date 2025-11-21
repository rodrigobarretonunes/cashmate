from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import UserCreate, UserLogin, TokenResponse,TransactionCreate
from models import User, Transaction
from fastapi import HTTPException
from jwt import encode, decode
import os 
import dotenv
from datetime import datetime, timedelta, timezone
from utils import create_access_token


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
    

def query_all_transactions(db: Session):
    try:
        stmt = select(Transaction)
        user_transactions = db.execute(stmt).scalars().all()
        return user_transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def query_transaction_by_id(db: Session, transaction_id: int):
    try:
        stmt = select(Transaction).where(Transaction.id == transaction_id)
        selected_transaction = db.execute(stmt).scalars().first()
        return selected_transaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def create_transaction(db,new_transaction,user_id:int):
    try:
        db_transaction = Transaction(
            user_id=user_id,
            owner_amount=new_transaction.owner_amount,
            type=new_transaction.type,
            description=new_transaction.description,
            category=new_transaction.category,
            is_recurring=new_transaction.is_recurring,
            end_date=new_transaction.end_date,
            counterparty_username=new_transaction.counterparty_username,
            counterparty_id=new_transaction.counterparty_id,
            is_shared=new_transaction.is_shared,
            counterparty=new_transaction.counterparty,
            counterparty_ratio=new_transaction.counterparty_ratio,
            counterparty_amount=new_transaction.counterparty_amount,
            expiration_time=new_transaction.expiration_time
        )
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction
    except Exception as e:
        import traceback
        error_detail = f"Error creating transaction: {str(e)} | {traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_detail)

def update_transaction(db:Session, db_transaction:Transaction, updated_transaction:Transaction):
    try:
        for var,value in vars(updated_transaction).items():
            setattr(db_transaction, var, value) if value else None
            db.commit()
            db.refresh(db_transaction)
            return db_transaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)+"Something went wrong when editing transaction")

def delete_transaction(db:Session, transaction_id:int):
    try:
        selected_transaction = query_transaction_by_id(db,transaction_id)
        if not selected_transaction:
            raise HTTPException(status_code=404, detail="Transaction not found")
        db.delete(selected_transaction)
        db.commit()
        return {"detail":"Transaction deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)+"Something went wrong when deleting transaction")

