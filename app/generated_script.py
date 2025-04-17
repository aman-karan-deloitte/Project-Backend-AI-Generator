import os

def create_folder_structure(project_root):
    folders = [
        'app',
        'app/api',
        'app/api/routes',
        'app/models',
        'app/services',
        'tests'
    ]
    for folder in folders:
        path = os.path.join(project_root, folder)
        if not os.path.exists(path):
            os.makedirs(path)

def create_files(project_root):
    files = [
        'app/api/routes/user.py',
        'app/api/routes/item.py',
        'app/api/routes/__init__.py',
        'app/models/user.py',
        'app/models/item.py',
        'app/models/__init__.py',
        'app/services/__init__.py',
        'app/database.py',
        'app/main.py',
        'tests/__init__.py',
        'Dockerfile',
        'requirements.txt',
        '.env',
        'README.md'
    ]
    for file in files:
        path = os.path.join(project_root, file)
        if not os.path.exists(path):
            open(path, 'w').close()

def populate_files(project_root):
    # app/api/routes/user.py
    with open(os.path.join(project_root, 'app/api/routes/user.py'), 'w') as f:
        f.write('from fastapi import APIRouter\n')
        f.write('from pydantic import BaseModel\n')
        f.write('from sqlalchemy import Column, Integer, String\n')
        f.write('from sqlalchemy.ext.declarative import declarative_base\n')
        f.write('from sqlalchemy.orm import sessionmaker\n')
        f.write('\n')
        f.write('router = APIRouter()\n')
        f.write('\n')
        f.write('class User(BaseModel):\n')
        f.write('    id: int\n')
        f.write('    name: str\n')
        f.write('    email: str\n')
        f.write('\n')
        f.write('@router.get("/api/auth/user")\n')
        f.write('def get_user():\n')
        f.write('    return {"message": "Hello, World!"}\n')

    # app/api/routes/item.py
    with open(os.path.join(project_root, 'app/api/routes/item.py'), 'w') as f:
        f.write('from fastapi import APIRouter\n')
        f.write('from pydantic import BaseModel\n')
        f.write('from sqlalchemy import Column, Integer, String\n')
        f.write('from sqlalchemy.ext.declarative import declarative_base\n')
        f.write('from sqlalchemy.orm import sessionmaker\n')
        f.write('\n')
        f.write('router = APIRouter()\n')
        f.write('\n')
        f.write('class Item(BaseModel):\n')
        f.write('    id: int\n')
        f.write('    name: str\n')
        f.write('    description: str\n')
        f.write('\n')
        f.write('@router.get("/api/items")\n')
        f.write('def get_items():\n')
        f.write('    return {"message": "Hello, World!"}\n')

    # app/models/user.py
    with open(os.path.join(project_root, 'app/models/user.py'), 'w') as f:
        f.write('from sqlalchemy import Column, Integer, String\n')
        f.write('from sqlalchemy.ext.declarative import declarative_base\n')
        f.write('\n')
        f.write('Base = declarative_base()\n')
        f.write('\n')
        f.write('class User(Base):\n')
        f.write('    __tablename__ = "users"\n')
        f.write('    id = Column(Integer, primary_key=True)\n')
        f.write('    name = Column(String)\n')
        f.write('    email = Column(String)\n')

    # app/models/item.py
    with open(os.path.join(project_root, 'app/models/item.py'), 'w') as f:
        f.write('from sqlalchemy import Column, Integer, String\n')
        f.write('from sqlalchemy.ext.declarative import declarative_base\n')
        f.write('\n')
        f.write('Base = declarative_base()\n')
        f.write('\n')
        f.write('class Item(Base):\n')
        f.write('    __tablename__ = "items"\n')
        f.write('    id = Column(Integer, primary_key=True)\n')
        f.write('    name = Column(String)\n')
        f.write('    description = Column(String)\n')

    # app/services/__init__.py
    with open(os.path.join(project_root, 'app/services/__init__.py'), 'w') as f:
        f.write('from .user_service import UserService\n')
        f.write('from .item_service import ItemService\n')

    # app/database.py
    with open(os.path.join(project_root, 'app/database.py'), 'w') as f:
        f.write('from sqlalchemy import create_engine\n')
        f.write('from sqlalchemy.orm import sessionmaker\n')
        f.write('\n')
        f.write('engine = create_engine("postgresql://user:password@host:port/dbname")\n')
        f.write('Session = sessionmaker(bind=engine)\n')
        f.write('session = Session()\n')

    # app/main.py
    with open(os.path.join(project_root, 'app/main.py'), 'w') as f:
        f.write('from fastapi import FastAPI\n')
        f.write('from app.api.routes import user\n')
        f.write('from app.api.routes import item\n')
        f.write('\n')
        f.write('app = FastAPI()\n')
        f.write('\n')
        f.write('app.include_router(user.router)\n')
        f.write('app.include_router(item.router)\n')

    # tests/__init__.py
    with open(os.path.join(project_root, 'tests/__init__.py'), 'w') as f:
        f.write('from unittest import TestCase\n')
        f.write('\n')
        f.write('class TestUser(TestCase):\n')
        f.write('    def test_get_user(self):\n')
        f.write('        pass\n')

    # Dockerfile
    with open(os.path.join(project_root, 'Dockerfile'), 'w') as f:
        f.write('FROM python:3.9-slim\n')
        f.write('WORKDIR /app\n')
        f.write('COPY requirements.txt .\n')
        f.write('RUN pip install -r requirements.txt\n')
        f.write('COPY . .\n')
        f.write('CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]\n')

    # requirements.txt
    with open(os.path.join(project_root, 'requirements.txt'), 'w') as f:
        f.write('fastapi\n')
        f.write('pydantic\n')
        f.write('sqlalchemy\n')
        f.write('uvicorn\n')

    # .env
    with open(os.path.join(project_root, '.env'), 'w') as f:
        f.write('DB_HOST=localhost\n')
        f.write('DB_PORT=5432\n')
        f.write('DB_NAME=mydb\n')
        f.write('DB_USER=myuser\n')
        f.write('DB_PASSWORD=mypassword\n')

    # README.md
    with open(os.path.join(project_root, 'README.md'), 'w') as f:
        f.write('# My Project\n')
        f.write('This is my project.\n')

project_root = os.getcwd()
create_folder_structure(project_root)
create_files(project_root)
populate_files(project_root)