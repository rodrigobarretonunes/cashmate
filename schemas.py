from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List         
from datetime import datetime 

# ========================
#       USERS
# ========================

class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)


class UserRead(BaseModel):
    id:int
    email:EmailStr
    username:str
    is_active:bool
    created_at:datetime
    
    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    message: Optional[str] = "Login Successful"








