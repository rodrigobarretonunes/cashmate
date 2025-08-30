from sqlalchemy import Column, Integer, String, Date, Numeric, Boolean, Enum
from sqlalchemy.orm import declarative_base
import enum
from .db import Base


#Tipos de transação

class TransactionType(str,enum.Enum):
    income = 'income'
    expense = 'expense'
    fixed = 'fixed'


class Transaction(Base):
    __tablename__ = "Transactions"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String,nullable=False)
    amount = Column(Numeric(12,2),nullable=False)
    date = Column(Date,nullable=False)
    type = Column(Enum(TransactionType),nullable=False)
    is_fixed = Column(Boolean,default=False)
    category = Column(String, nullable=True)
    user_id = Column(Integer, nullable=False,index=True)


