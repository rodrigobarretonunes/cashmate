from pydantic import BaseModel, Field
from typing import Optional, List         
from datetime import datetime 

# ========================
#       USERS
# ========================

class SchemaUserRegister(BaseModel):
    username: str
    email: str
    password: str


class SchemaUserLogin(BaseModel):
    username: str
    password: str
    class Config:
        orm_mode = True



