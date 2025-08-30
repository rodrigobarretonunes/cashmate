
# `README.md` (versão inicial)

```markdown
# CashMate

CashMate é um aplicativo simples de **gestão de finanças pessoais** desenvolvido com **FastAPI**, **SQLAlchemy** e **SQLite**.  
O objetivo é substituir planilhas Excel, permitindo que você e sua esposa possam registrar receitas, despesas e despesas fixas, além de consultar resumos mensais de maneira simples.

---

## Status atual do projeto

Até o momento, o projeto possui:

- **Ambiente virtual** configurado (`venv`) com as dependências:
  - FastAPI
  - Uvicorn
  - SQLAlchemy
  - Pydantic
- **Estrutura de pastas organizada**, seguindo boas práticas para facilitar manutenção e escalabilidade:
```

core/
├─ **init**.py
├─ main.py
├─ db.py
├─ models.py
├─ schemas.py
├─ crud.py
├─ services.py
└─ routers/
├─ **init**.py
└─ transactions.py

````
- **Configuração inicial do banco de dados** (`db.py`) usando SQLite:
- Engine de conexão
- SessionLocal para criar sessões de banco
- Base para os modelos (tabelas)
- Dependência `get_db` para injeção do banco nas rotas

---

## Próximos passos planejados

- Criar **modelos** (tabelas) para transações financeiras no `models.py`.
- Criar **schemas** (`schemas.py`) para validação e serialização de dados que entram e saem da API.
- Implementar **CRUD** (`crud.py`) para adicionar, listar, atualizar e deletar transações.
- Criar **services** (`services.py`) para lógica de negócio, como cálculo de resumo mensal.
- Implementar **routers** (`routers/transactions.py`) para expor endpoints da API.
- Desenvolver **frontend mínimo** (HTML + JS) para interagir com a API.
- Garantir que a estrutura siga princípios **SOLID**, facilitando upgrades futuros.

---

## Como rodar o projeto (até agora)

1. Criar e ativar o ambiente virtual:
 ```bash
 python -m venv venv
 source venv/bin/activate  # Linux/Mac
 .\venv\Scripts\activate   # Windows
````

2. Instalar dependências (via `uv`):

   ```bash
   uv add fastapi uvicorn[standard] sqlalchemy pydantic
   ```
3. Confirmar que a pasta `core/` com os arquivos básicos (`main.py`, `db.py`, etc.) está criada.

> Nota: Até o momento, a API não possui endpoints implementados. O próximo passo será criar os **modelos** e **tabelas** de transações.

```

---
