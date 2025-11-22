from pydantic import BaseModel, Field, EmailStr        
from datetime import datetime 

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

