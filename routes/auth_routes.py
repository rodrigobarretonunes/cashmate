from fastapi import APIRouter
from crud import get_password_hash, create_user, verify_password, verify_if_user_exists, login_user
from schemas import UserCreate, UserLogin, UserRead
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from database import get_db 






router = APIRouter(prefix="/auth", tags=["auth"])


#Endpoint to register a new user

@router.post("/register",response_model=UserRead)
async def register_user(user:UserCreate, db: Session=Depends(get_db)):
    # verify if user already exists
    existing_user = verify_if_user_exists(db, user.username)
    if existing_user:
        raise HTTPException (status_code=400, detail='User already exists')
    # hash the password 
    hashed_password = get_password_hash(user.password)
    #register the user 
    new_user = await create_user(db, user, hashed_password)
    return new_user


# Endpoint to login a user 
@router.post("login")
async def login_user_endpoint(user:UserLogin, db: Session=Depends(get_db)):
    token = await login_user(db,user)
    return token
