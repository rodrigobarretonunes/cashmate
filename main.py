from fastapi import FastAPI
from routes import auth_routes
from database import init_db

app = FastAPI()
init_db()

app.include_router(auth_routes.router)
