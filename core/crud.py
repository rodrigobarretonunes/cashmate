from werkzeug.security import generate_password_hash, check_password_hash
from schemas import UserCreate
from sqlalchemy.orm import Session
from models import User
from sqlalchemy import select
import jwt
from datetime import datetime, timedelta,timezone
from dotenv import load_dotenv
import os 
from fastapi import HTTPException


load_dotenv()


def hash_password(password: str) -> str:
    return generate_password_hash(password)


def create_user(db:Session,user:UserCreate,hashed_password:str):
    new_user=User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def get_token(data:dict):
    to_encode = data.copy()
    now_utc = datetime.now(timezone.utc)
    expire = now_utc + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",60)))
    to_encode.update({"exp":expire})
    try:
        secret_key = os.getenv("SECRET_KEY")
        token = jwt.encode(to_encode,secret_key,algorithm=os.getenv("ALGORITHM"))
        return token
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Erro ao gerar o token")
    




def verify_token(token: str):
    ...

#Função que verifica se o usuario existe no banco de dados 
def verify_if_user_exists(db:Session,username:str):
    stmt = select(User).where(User.username==username)
    return db.execute(stmt).scalars().first()