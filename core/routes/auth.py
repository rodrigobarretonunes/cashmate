from fastapi import APIRouter, HTTPException, Depends
import schemas
from crud import hash_password, create_user
from sqlalchemy.orm import Session
from database import get_db





router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register",response_model=schemas.UserRead)
async def register(user:schemas.UserCreate, db:Session=Depends(get_db)):

    hashed_password = hash_password(user.password)
    new_user = await create_user(db=db,user=user,hashed_password=hashed_password)
    return new_user




