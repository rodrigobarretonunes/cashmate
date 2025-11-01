from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship

# Base do SQLAlchemy
class Base(DeclarativeBase):
    pass


# ========================
#       USERS
# ========================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False) # Nome de usuário
    email = Column(String, unique=True, index=True, nullable=True, default = None)    # Email do usuário
    hashed_password = Column(String, nullable=False)  # Senha criptografada
    balance = Column(Float, default=0.0, nullable=False)  # Saldo total atual do usuário
    is_active = Column(Boolean, default=True, nullable=False)  # Se o usuário está ativo
    is_superuser = Column(Boolean, default=False, nullable=False)  # Permissão administrativa
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)  # Data de criação
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())  # Atualizado automaticamente

    # Relação com transações
    transactions = relationship("Transaction", back_populates="user")



# ========================
#     TRANSACTIONS
# ========================
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Relacionamento com o usuário

    owner_amount = Column(Float, nullable=False)  # Valor da transação
    type = Column(String, nullable=False)  # 'income' (entrada) ou 'expense' (saída)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)  # Data da criação
    description = Column(String, nullable=True)  # Exemplo: 'grocery shopping'
    category = Column(String, nullable=True)  # Exemplo: 'food', 'rent', 'salary', etc.

    is_recurring = Column(Boolean, default=False, nullable=False)  # Se é uma despesa/receita recorrente
    end_date = Column(DateTime(timezone=True), nullable=True)  # Caso tenha data de término (para transações recorrentes)

    counterparty_username = Column(String, ForeignKey("users.username"), nullable=True)  #
    is_shared = Column(Boolean, default=False, nullable=False)  # Se a transação é compartilhada com alguém
    counterparty = Column(String, nullable=True)  # Pessoa com quem compartilha (ex: 'Maria')
    counterparty_ratio = Column(Float, nullable=True)  # Percentual da divisão (ex: 50%)
    counterparty_amount = Column(Float, nullable=True)  # Valor correspondente à outra parte
    accepted_by_counterparty = Column(Boolean, default=False, nullable=False)  # Se a outra parte aceitou o compartilhamento
    expiration_time = Column(DateTime,nullable=True)  # Até quando a outra parte pode aceitar a transação
    # Relação inversa
    user = relationship("User", back_populates="transactions")

