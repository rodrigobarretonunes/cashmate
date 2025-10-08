from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List         
from datetime import datetime 


# -----------------------------
# Usuários
# -----------------------------

class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)


class UserRead(BaseModel):
    id:int
    email:EmailStr
    username:str
    is_active:bool
    created_at:datetime
    
    class Config:
        from_attributes=True
    

class UserLogin(BaseModel):
    username:str
    password:str


class UserToken(BaseModel):
   access_token:str
   token_type:str
   msg:str

   class Config:
        from_attributes=True


# -----------------------------
# Transações
# -----------------------------

class TransactionCreate(BaseModel):
    description : str
    type : str
    owner_amount : float
    category : Optional[str] = None
    is_shared : Optional[bool] = False
    counterparty_username: Optional[int] = None
    counterparty_ratio : Optional[float] = None
    counterparty_amount : Optional[float] = None
    owner_ratio : Optional[float] = None
    is_recurring : Optional[bool] = False
    end_date : Optional[datetime] = None
    accepted_by_counterparty : Optional[bool] = False
    expiration_time : Optional[datetime] = None


class TransactionRead(BaseModel):
    id : int
    user_id : int
    owner_amount : float
    type : str
    category : Optional[str] = None
    description: str
    created_at : datetime
    is_shared : Optional[bool] = False
    counterparty_username : Optional[int] = None
    counterparty_ratio : Optional[float] = None
    counterparty_amount : Optional[float] = None
    owner_ratio : Optional[float] = None
    is_recurring : Optional[bool] = False
    end_date : Optional[datetime] = None
    
    
    class Config:
        from_attributes:True


# -----------------------------
# Combinações úteis
# -----------------------------
class UserWithTransactions(UserRead):
    transactions: List[TransactionRead] = []



