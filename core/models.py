from sqlalchemy import Column, String, Integer, Boolean, DateTime,Float,ForeignKey
from sqlalchemy.orm import declarative_base,relationship
from datetime import timezone, datetime
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
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="transactions")

