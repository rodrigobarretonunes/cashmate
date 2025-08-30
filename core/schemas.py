from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import date
from typing import Optional


class TransactionBase(BaseModel):
    description:str=Field(...)
    amount:Decimal=Field(...)
    date:date
    type:str=Field(...)
    is_fixed:Optional[bool]=False
    category:Optional[str]=None
    use_id:int

class TransactionCreate(TransactionBase):
    pass

class TransactionRead(TransactionBase):
    
