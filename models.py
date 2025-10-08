from sqlalchemy import Column, String, Integer, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import timezone, datetime
from typing import Optional

from database import Base



class User(Base):
    __tablename__ = "users_table"
    id = Column(Integer, primary_key=True, index=True)
    email =  Column(String, unique=True, nullable=False,index=True)
    username = Column(String, unique=True,nullable=False,index=True)
    hashed_password = Column(String, nullable=True)
    balance = Column(Float,default=0.0)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    transactions = relationship("Transaction", back_populates="user")



class Transaction(Base):
    __tablename__ = "transactions_table"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users_table.id"), nullable=False)
    owner_amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    owner_ratio = Column(Float, nullable=True)
    category = Column(String, nullable=True)
    is_recurring = Column(Boolean, default=False, nullable=False)  # indica se é fixa
    end_date = Column(DateTime, nullable=True)  # até quando deve se repetir
    counterparty_username = Column(String, ForeignKey("users_table.id"), nullable=True)
    counterparty_ratio = Column(Float, nullable=True)
    counterparty_amount = Column(Float,nullable=True)
    accepted_by_counterparty = Column(Boolean, default=False)
    expiration_time = Column(DateTime,nullable=True)
    user = relationship("User", back_populates="transactions")



    