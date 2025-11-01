from fastapi import FastAPI
from routes import auth_routers

app = FastAPI()

app.include_router(auth_routers.router)