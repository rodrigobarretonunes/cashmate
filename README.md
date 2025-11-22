# Cashmate 🚀

Welcome to **Cashmate**, your finance transaction management app built with **FastAPI**! 💸

The goal of this project is simple: organize, track, and secure user transactions in a modular, clean, and scalable way.

---

## 🗂 Project Structure

The project is divided into two main parts:

### 1️⃣ `api/`

All **business logic** and endpoints. Each module represents a feature of the app:

* **auth** → User authentication, login, JWT token creation, credential verification
* **wallet** → Transaction management: create, update, delete, and query transactions
* Each module has its own `__init__.py` for clean imports without navigating deep folder paths

### 2️⃣ `core/`

The **core of the app**, with essential and global functionalities:

* **database.py** → SQLAlchemy setup, Base, engine, and session
* **security.py** → JWT token creation and validation, password hashing and verification
* Other global utilities that don’t belong to a specific module

---

## ⚡ Features

* User registration and login with hashed passwords
* JWT-based authentication and authorization
* CRUD operations for transactions
* Organized modular structure for easy scaling and maintenance

---

## 🚀 Getting Started

1. Clone the repo:

```bash
git clone https://github.com/yourusername/cashmate.git
cd cashmate
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your keys:

```
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run the app:

```bash
uvicorn main:app --reload
```

6. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧩 Why Cashmate?

We wanted a **lightweight, modular, and clean architecture** for managing financial transactions.
Everything is organized in packages so you can import functions easily and scale the app without messy circular imports.

---

## 💡 Notes

* The project uses **FastAPI**, **SQLAlchemy**, **Passlib** for password hashing, and **PyJWT** for token management.
* Modular design helps avoid circular imports and keeps your codebase clean.
* Each endpoint and module is designed to be **self-contained** and easy to test.

---

## 📌 License

This project is free to use and modify.

---

Made with ❤️ and Python by your dev team.
