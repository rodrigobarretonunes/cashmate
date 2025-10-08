from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schemas
from services import split_transaction


router = APIRouter(prefix="/transaction", tags=["transaction"])



"""
Aqui eu preciso criar as rotas de transações: 
Uma rota que ira criar uma nova transação
Uma rota que ira enviar todas as transações do usuario
Uma rota pra excluir uma transação 
Uma rota pra editar uma transação 
"""

@router.post("/add_transaction",response_model=schemas.TransactionCreate)
def add_transaction(transaction:schemas.TransactionCreate, db:Session=Depends(get_db)): 
    return split_transaction(db,transaction=transaction)

