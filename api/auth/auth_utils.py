from sqlalchemy.orm import Session 
from fastapi import HTTPException, Request
from sqlalchemy import select
from jose import JWTError, jwt
import os
from core.security import SECRET_KEY, ALGORITHM
from .auth_models import User 



def get_current_user(request:Request, db:Session):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    try:
        token_type,token = auth_header.split(" ")
        if token_type.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid token type")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        stmt = select(User).where(User.id == user_id)
        user = db.execute(stmt).scalars().first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Token decode error")