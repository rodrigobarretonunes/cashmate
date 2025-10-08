from werkzeug.security import generate_password_hash, check_password_hash
from schemas import UserCreate,TransactionCreate
from sqlalchemy.orm import Session
from models import User, Transaction
from sqlalchemy import select
import jwt
from datetime import datetime, timedelta,timezone
from dotenv import load_dotenv
import os 
from fastapi import HTTPException,status
from jose import JWTError, jwt, ExpiredSignatureError



load_dotenv()


# Função que gera a hash da senha
def hash_password(password: str) -> str:
    return generate_password_hash(password)


# Função que cria um novo usuário
def create_user(db:Session,user:UserCreate,hashed_password:str):
    new_user=User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Função que gera o JWT
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


#Função que verifica o JWT
def verify_token(token: str):
    secret_key = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM")

    try:
        payload = jwt.decode(token,secret_key,algorithms=[algorithm])
        user_id = payload["user_id"]
        username = payload["username"]
        if not user_id or not username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido ou expirado")
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token Invalido")
   

# Função que verifica se o usuario existe
def verify_if_user_exists(db:Session,username:str):
    stmt = select(User).where(User.username==username)
    return db.execute(stmt).scalars().first()


# Função que monta a transação
def build_transaction(user_id, transaction_data):
    new_transaction = Transaction(
        user_id = user_id,
        owner_amount = transaction_data.owner_amount,
        type = transaction_data.type,
        description = transaction_data.description,
        category = transaction_data.category,
        is_shared = transaction_data.is_shared,
        counterparty_username = transaction_data.counterparty_username,
        counterparty_ratio = transaction_data.counterparty_ratio,
        counterparty_amount = transaction_data.counterparty_amount,
        owner_ratio = transaction_data.owner_ratio,
        is_recurring = transaction_data.is_recurring,
        end_date = transaction_data.end_date,
        accepted_by_counterparty = transaction_data.accepted_by_counterparty,
        expiration_time = transaction_data.expiration_time)
    return new_transaction


# Função que cria a transação
def create_transaction(db:Session,transaction:TransactionCreate, counterparty:User):
    try:
        if counterparty is None:
            new_owner_transaction = build_transaction(transaction.user_id,transaction_data=transaction)
            db.add(new_owner_transaction)
            db.commit()
            db.refresh(new_owner_transaction)
        else:
            new_owner_transaction = build_transaction(transaction.user_id,transaction_data=transaction)
            new_counterparty_transaction = build_transaction(counterparty.user_id,transaction_data=transaction)
            db.add(new_counterparty_transaction)
            db.commit()
            db.refresh(new_counterparty_transaction)
        return new_owner_transaction
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao criar a transação")





