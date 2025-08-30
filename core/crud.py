from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date


def create_transaction(db:Session, transaction:schemas.TransactionCreate):
    db_transaction = models.Transaction(
        description=transaction.description,
        amount=transaction.amount,
        date=transaction.date,
        type=transaction.type,
        is_fixed=transaction.is_fixed,
        category=transaction.category,
        notes=transaction.notes,
        user_id=transaction.user_id
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db.transaction)
    return db_transaction


def get_transactions(db:Session,user_id=int):
    return db.query(models.Transaction).filter(models.Transaction.user_id==user_id).all()


def get_transaction(db:Session,transaction_id=int):
    return db.query(models.Transaction).filter(models.Transaction.id==transaction_id).first()


def delete_transaction(db:Session,transaction_id:int):
    transaction=db.query('models.Transaction').filter(models.Transaction.id==transaction_id).first()
    if transaction:
        db.delete(transaction)
        db.commit()
    return transaction

