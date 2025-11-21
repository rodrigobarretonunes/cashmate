from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime, timezone 
from core.database import Base


# ========================
#       USERS
# ========================
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



# ========================
#     TRANSACTIONS
# ========================
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users_table.id"), nullable=False)  # Relacionamento com o usuário

    owner_amount = Column(Float, nullable=False)  # Valor da transação
    type = Column(String, nullable=False)  # 'income' (entrada) ou 'expense' (saída)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)  # Data da criação
    description = Column(String, nullable=True)  # Exemplo: 'grocery shopping'
    category = Column(String, nullable=True)  # Exemplo: 'food', 'rent', 'salary', etc.

    is_recurring = Column(Boolean, default=False, nullable=False)  # Se é uma despesa/receita recorrente
    end_date = Column(DateTime(timezone=True), nullable=True)  # Caso tenha data de término (para transações recorrentes)

    counterparty_username = Column(String, nullable=True)
    counterparty_id = Column(Integer, nullable=True)
    is_shared = Column(Boolean, default=False, nullable=False)  # Se a transação é compartilhada com alguém
    counterparty = Column(String, nullable=True)  # Pessoa com quem compartilha (ex: 'Maria')
    counterparty_ratio = Column(Float, nullable=True)  # Percentual da divisão (ex: 50%)
    counterparty_amount = Column(Float, nullable=True)  # Valor correspondente à outra parte
    accepted_by_counterparty = Column(Boolean, default=False, nullable=False)  # Se a outra parte aceitou o compartilhamento
    expiration_time = Column(DateTime,nullable=True)  # Até quando a outra parte pode aceitar a transação
    # Relação inversa
    user = relationship("User", back_populates="transactions")

