from pydantic import BaseModel, EmailStr 
from typing import Optional, List         
from datetime import datetime 


# -----------------------------
# Usuários
# -----------------------------

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserRead(BaseModel):
    id:int
    email:EmailStr
    username:str
    is_active:bool
    created_at:datetime
    
    class Config:
        orm_mode=True
    

class UserLogin(BaseModel):
    username:str
    password:str


class UserToken(BaseModel):
   access_token:str
   token_type:str

   class Config:
        orm_mode=True


# -----------------------------
# Transações
# -----------------------------

class TransactionCreate(BaseModel):
    description = str
    type = str
    amount = float

class TransactionRead(BaseModel):
    id = int
    user_id = int
    amount = float
    type = str
    category = Optional[str] = None
    description: str
    created_at = datetime
    
    class Config:
        orm_mode=True


# -----------------------------
# Combinações úteis
# -----------------------------
class UserWithTransactions(UserRead):
    transactions: List[TransactionRead] = []



