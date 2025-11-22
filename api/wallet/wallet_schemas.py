from pydantic import BaseModel
from typing import Optional        
from datetime import datetime 


class TransactionCreate(BaseModel):
    user_id: int
    owner_amount: float
    type: str  # 'income' ou 'expense'
    created_at: datetime
    description: Optional[str] = None
    category: Optional[str] = None
    is_recurring: Optional[bool] = False
    end_date: Optional[datetime] = None




# Schema para leitura de transações (retorno da API)
class TransactionRead(BaseModel):
    id: int
    user_id: int
    owner_amount: float
    type:str
    created_at: datetime
    description: Optional[str] = None
    category: Optional[str] = None
    is_recurring: bool
    end_date: Optional [datetime] = None
    model_config = {"from_attributes": True}

# Schema para atualização de transações

class TransactionUpdate(BaseModel):
    owner_amout : Optional[float] = None
    type: Optional[str] = None
    description: Optional[str] = None
    category: Optional [str] = None
    is_recurring: Optional[bool] = None
    end_date: Optional[datetime] = None
    model_config = {"from_attributes": True}




