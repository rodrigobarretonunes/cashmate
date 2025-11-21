from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth_routes, transaction_routes
from database import init_db

app = FastAPI()
init_db()

# Configuração de CORS
origins = [
    "http://localhost:5173",  # endereço do seu frontend Vite
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # quem pode acessar
    allow_credentials=True,     # cookies/autenticação
    allow_methods=["*"],        # permite GET, POST, OPTIONS...
    allow_headers=["*"],        # permite qualquer header
)

# Inclui as rotas de autenticação
app.include_router(auth_routes.router)
app.include_router(transaction_routes.router)

