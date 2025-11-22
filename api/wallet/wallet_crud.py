from sqlalchemy.orm import Session
from sqlalchemy import select
from .wallet_models import Transaction
from fastapi import HTTPException


async def query_all_transactions(db: Session):
    try:
        stmt = select(Transaction)
        user_transactions = db.execute(stmt).scalars().all()
        return user_transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def query_transaction_by_id(db: Session, transaction_id: int):
    try:
        stmt = select(Transaction).where(Transaction.id == transaction_id)
        selected_transaction = db.execute(stmt).scalars().first()
        return selected_transaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def create_transaction(db,new_transaction,user_id:int):
    try:
        db_transaction = Transaction(
            user_id=user_id,
            owner_amount=new_transaction.owner_amount,
            type=new_transaction.type,
            description=new_transaction.description,
            category=new_transaction.category,
            is_recurring=new_transaction.is_recurring,
            end_date=new_transaction.end_date,
            counterparty_username=new_transaction.counterparty_username,
            counterparty_id=new_transaction.counterparty_id,
            is_shared=new_transaction.is_shared,
            counterparty=new_transaction.counterparty,
            counterparty_ratio=new_transaction.counterparty_ratio,
            counterparty_amount=new_transaction.counterparty_amount,
            expiration_time=new_transaction.expiration_time
        )
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction
    except Exception as e:
        import traceback
        error_detail = f"Error creating transaction: {str(e)} | {traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_detail)

async def update_transaction(db:Session, db_transaction:Transaction, updated_transaction:Transaction):
    try:
        for var,value in vars(updated_transaction).items():
            setattr(db_transaction, var, value) if value else None
            db.commit()
            db.refresh(db_transaction)
            return db_transaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)+"Something went wrong when editing transaction")

async def delete_transaction(db:Session, transaction_id:int):
    try:
        selected_transaction = query_transaction_by_id(db,transaction_id)
        if not selected_transaction:
            raise HTTPException(status_code=404, detail="Transaction not found")
        db.delete(selected_transaction)
        db.commit()
        return {"detail":"Transaction deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)+"Something went wrong when deleting transaction")
