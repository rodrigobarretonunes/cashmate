from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime, timezone 
from core.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users_table.id"), nullable=False)

    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    description = Column(String, nullable=True)
    category = Column(String, nullable=True)
    is_recurring = Column(Boolean, default=False, nullable=False)

    # relação com user
    user = relationship("User", back_populates="transactions")