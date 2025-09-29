from fastapi import FastAPI
from routes import auth, transactions
from database import init_db


app = FastAPI()
init_db()

app.include_router(auth.router)
app.include_router(transactions.router)


