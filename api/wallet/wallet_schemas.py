from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List         
from datetime import datetime 


class TransactionCreate(BaseModel):
    owner_amount: float
    type: str  # 'income' ou 'expense'
    description: Optional[str] = None
    category: Optional[str] = None
    is_recurring: Optional[bool] = False
    end_date: Optional[datetime] = None
    counterparty_username: Optional[str] = None
    counterparty_id: Optional[int] = None
    is_shared: Optional[bool] = False
    counterparty: Optional[str] = None
    counterparty_ratio: Optional[float] = None
    counterparty_amount: Optional[float] = None
    expiration_time: Optional[datetime] = None



# Schema para leitura de transações (retorno da API)
class TransactionRead(BaseModel):
    id: int
    user_id: int
    owner_amount: float
    type: str
    created_at: datetime
    description: Optional[str] = None
    category: Optional[str] = None
    is_recurring: bool
    end_date: Optional[datetime] = None
    counterparty_username: Optional[str] = None
    counterparty_id: Optional[int] = None
    is_shared: bool
    counterparty: Optional[str] = None
    counterparty_ratio: Optional[float] = None
    counterparty_amount: Optional[float] = None
    accepted_by_counterparty: bool
    expiration_time: Optional[datetime] = None

    model_config = {"from_attributes": True}



