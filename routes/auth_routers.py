from fastapi import APIRouter


router = APIRouter()


#Essa sera a primeira rota ligada a cadastro de um usuario 

@router.post("/register")
async def register_user():
    ...


