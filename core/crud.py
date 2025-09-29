from werkzeug.security import generate_password_hash, check_password_hash
from schemas import UserCreate
from sqlalchemy.orm import Session
from models import User



def hash_password(password: str) -> str:
    return generate_password_hash(password)


async def create_user(db:Session,user:UserCreate,hashed_password:str):
    new_user=User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



    