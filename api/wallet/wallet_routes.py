# This file is responsible for routes user's transaction operations

from fastapi import APIRouter, Depends, HTTPException,Request
from sqlalchemy.orm import Session 
from core.database import get_db
from api.auth.auth_models import Transaction
from .wallet_schemas import TransactionCreate, TransactionRead
from .wallet_crud import query_all_transactions, query_transaction_by_id,create_transaction,update_transaction,delete_transaction
from ..auth.auth_utils import token_validation, get_current_user



router = APIRouter(prefix='/transactions', tags=['transactions'])

# Endpoint to create a new transaction
#List of routes needed for the application: create, read, update, delete, invite to share, share transaction

@router.post("/all_transactions", response_model=list[TransactionRead])
async def get_transactions_endpoint(request, db: Session=Depends(get_db)):
    if not token_validation(request):
        raise HTTPException(status_code=401, detail="Invalid token")
    try:
        transactions = query_all_transactions(db=db)
        return transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/transaction/create", response_model=TransactionRead)
async def create_transaction_endpoint(request: Request, transaction:TransactionCreate, db: Session=Depends(get_db)):
    if not token_validation(request):
        raise HTTPException(status_code=401, detail="Invalid token")
    try:
        user =get_current_user(request,db)
        new_transaction = create_transaction(db=db,new_transaction=transaction,user_id=user.id)
        return new_transaction
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.delete("/transaction/delete/{transaction_id}", response_model=dict)
async def delete_transaction_endpoint(request:Request, transaction_id:int, db:Session=Depends(get_db)):
    if not token_validation(request):
        raise HTTPException(status_code=401, detail="Invalid token")
    try:
        delete_transaction(db=db,transaction_id=transaction_id)
        return{"detail":"Transaction deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.put("/transaction/update/{transaction_id}",response_model=TransactionRead)
async def update_transaction_endpoint(request,transaction_id:int,updated_transaction:TransactionCreate,db:Session=Depends(get_db)):
    if not token_validation(request):
        raise HTTPException(status_code=401, detail="Invalid token")
    try:
        db_transaction = query_transaction_by_id(db=db,transaction_id=transaction_id)
        if not db_transaction:
            raise HTTPException(status_code=404,detail="Transaction not found")
        updated_transaction = update_transaction(db=db,db_transaction=db_transaction,updated_transaction=updated_transaction)
        return updated_transaction
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))



    



