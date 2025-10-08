from fastapi import APIRouter, HTTPException, Depends
import schemas
from crud import hash_password, create_user,verify_if_user_exists,get_token
from sqlalchemy.orm import Session
from database import get_db
from werkzeug.security import check_password_hash






router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register",response_model=schemas.UserRead)
async def register(user:schemas.UserCreate, db:Session=Depends(get_db)):
    hashed_password = hash_password(user.password)
    new_user = create_user(db=db,user=user,hashed_password=hashed_password)
    return new_user




@router.post("/login",response_model=schemas.UserToken)
async def login(user:schemas.UserLogin,db:Session=Depends(get_db)):
    
    try: 
        existing_user = verify_if_user_exists(db,user.username)
        if existing_user:       
            pwhash= existing_user.hashed_password
            if check_password_hash(pwhash,user.password):
                data = {"id":existing_user.id, "username":existing_user.username}
                token = get_token(data)
                print(token)
                print(data)
                return {"access_token":token,"token_type":"Bearer","msg":"Token gerado com sucesso!"}
            else:
                raise HTTPException(status_code=400,detail="A sua senha esta incorreta!")
        else:
            raise HTTPException(status_code=400, detail="Username não encontrado, tente novamente!")

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Houve um problem com o seu login, recarregue a pagina e tente novamente.")

    

