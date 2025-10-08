from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import User, Transaction
from crud import verify_if_user_exists,create_transaction
from schemas import TransactionCreate


def split_transaction(db,transaction):
   
    try:
        if transaction.is_shared:
            counterparty = verify_if_user_exists(db,transaction.counterparty_username)
            if not counterparty:
                raise HTTPException(status_code=404,detail='Usuário com quem a transação será compartilhada não existe')
            if not transaction.owner_ratio or transaction.owner_ratio <= 0:
                raise HTTPException(status_code=400, detail='Por favor, forneça um valor valido para a divisão da transação.')
            if transaction.owner_ratio>=1:
                transaction.counterparty_ratio = 100 - transaction.owner_ratio
                transaction.counterparty_amount = transaction.owner_amount * (transaction.counterparty_ratio/100)
                transaction.owner_amount = transaction.owner_amount * (transaction.owner_ratio/100)
            return create_transaction(db,counterparty, transaction=transaction )
        else: 
            return create_transaction(db,None, transaction=transaction )
        
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao processar a transação compartilhada")
    


def send_shared_transaction_invite(shared_user,transaction):
    #Aqui eu vou implementar a lógica de enviar o convite para o usuario com quem a transação será compartilhada
    ...
    return True



