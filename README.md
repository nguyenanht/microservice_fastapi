# microservice_fastapi

## Part 1 Local Setup

1. `pip install poetry` (or safer, follow the instructions: https://python-poetry.org/docs/#installation)
2. Install dependencies `cd` into the directory where the `pyproject.toml` is located then `poetry install`
3. [UNIX]: Run the FastAPI server via poetry with the bash script: `poetry run ./entrypoint.sh`
4. [WINDOWS]: Run the FastAPI server via poetry with the Python command: `poetry run python app/main.py`
5. Open http://localhost:8001/

To stop the server, press CTRL+C


## 6 Database Setup with SQLAlchemy and Alembic
https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-7-sqlalchemy-database-setup/

SQLAlchemy is one of the most widely used and highest quality Python third-party libraries. It gives application developers easy ways to work with relational databases in their Python code.

SQLAlchemy is composed of two distinct components:

Core - a fully featured SQL abstraction toolkit
ORM (Object Relational Mapper) - which is optional

In this tutorial, we will make use of both components, though you can adapt the approach not to use the ORM.

```bash
.
├── alembic                    ----> NEW
│  ├── env.py
│  ├── README
│  ├── script.py.mako
│  └── versions
│     └── 238090727082_added_user_and_recipe_tables.py
├── alembic.ini                ----> NEW
├── app
│  ├── __init__.py
│  ├── backend_pre_start.py    ----> NEW
│  ├── crud                    ----> NEW
│  │  ├── __init__.py
│  │  ├── base.py
│  │  ├── crud_recipe.py
│  │  └── crud_user.py
│  ├── db                      ----> NEW
│  │  ├── __init__.py
│  │  ├── base.py
│  │  ├── base_class.py
│  │  ├── init_db.py
│  │  └── session.py
│  ├── deps.py                 ----> NEW
│  ├── initial_data.py
│  ├── main.py
│  ├── models                  ----> NEW
│  │  ├── __init__.py
│  │  ├── recipe.py
│  │  └── user.py
│  ├── recipe_data.py
│  ├── schemas
│  │  ├── __init__.py
│  │  ├── recipe.py
│  │  └── user.py
│  └── templates
│     └── index.html
├── poetry.lock_
├── prestart.sh
├── pyproject.toml
├── README.md
└── run.sh

```