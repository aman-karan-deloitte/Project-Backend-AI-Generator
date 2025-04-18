import os

def generate_project_structure():
    project_root = 'generated_project'
    os.mkdir(project_root)

    app_folder = os.path.join(project_root, 'app')
    os.mkdir(app_folder)

    api_folder = os.path.join(app_folder, 'api')
    os.mkdir(api_folder)

    routes_folder = os.path.join(api_folder, 'routes')
    os.mkdir(routes_folder)

    user_route = os.path.join(routes_folder, 'user.py')
    item_route = os.path.join(routes_folder, 'item.py')
    init_route = os.path.join(routes_folder, '__init__.py')

    with open(user_route, 'w') as f:
        f.write('from fastapi import APIRouter\nrouter = APIRouter()')

    with open(item_route, 'w') as f:
        f.write('from fastapi import APIRouter\nrouter = APIRouter()')

    with open(init_route, 'w') as f:
        f.write('')

    models_folder = os.path.join(app_folder, 'models')
    os.mkdir(models_folder)

    user_model = os.path.join(models_folder, 'user.py')
    item_model = os.path.join(models_folder, 'item.py')
    init_model = os.path.join(models_folder, '__init__.py')

    with open(user_model, 'w') as f:
        f.write('from pydantic import BaseModel\nclass User(BaseModel):\n    id: int\n    name: str')

    with open(item_model, 'w') as f:
        f.write('from pydantic import BaseModel\nclass Item(BaseModel):\n    id: int\n    name: str')

    with open(init_model, 'w') as f:
        f.write('')

    services_folder = os.path.join(app_folder, 'services')
    os.mkdir(services_folder)

    database_file = os.path.join(app_folder, 'database.py')
    with open(database_file, 'w') as f:
        f.write('from sqlalchemy import create_engine\nengine = create_engine("postgresql://user:password@host:port/dbname")')

    main_file = os.path.join(app_folder, 'main.py')
    with open(main_file, 'w') as f:
        f.write('from fastapi import FastAPI\napp = FastAPI()')

    tests_folder = os.path.join(project_root, 'tests')
    os.mkdir(tests_folder)

    test_main = os.path.join(tests_folder, 'test_main.py')
    with open(test_main, 'w') as f:
        f.write('import pytest\nfrom app.main import app\n@pytest.fixture\ndef test_app():\n    return app')

    docker_file = os.path.join(project_root, 'Dockerfile')
    with open(docker_file, 'w') as f:
        f.write('FROM python:3.9-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nCMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]')

    requirements_file = os.path.join(project_root, 'requirements.txt')
    with open(requirements_file, 'w') as f:
        f.write('fastapi\npydantic\nsqlalchemy\n')

    env_file = os.path.join(project_root, '.env')
    with open(env_file, 'w') as f:
        f.write('DB_HOST=localhost\nDB_PORT=5432\nDB_NAME=mydb\nDB_USER=myuser\nDB_PASSWORD=mypassword')

    readme_file = os.path.join(project_root, 'README.md')
    with open(readme_file, 'w') as f:
        f.write('# My Project\nThis is my project.')

    user_route = os.path.join(routes_folder, 'user.py')
    with open(user_route, 'a') as f:
        f.write('\n\nclass UserRoute:\n    def __init__(self, app):\n        self.app = app\n\n    def get_users(self):\n        return [{"id": 1, "name": "John"}]')

    item_route = os.path.join(routes_folder, 'item.py')
    with open(item_route, 'a') as f:
        f.write('\n\nclass ItemRoute:\n    def __init__(self, app):\n        self.app = app\n\n    def get_items(self):\n        return [{"id": 1, "name": "Item1"}]')

    main_file = os.path.join(app_folder, 'main.py')
    with open(main_file, 'a') as f:
        f.write('\n\nfrom app.api.routes import user, item\n\napp.include_router(user.router)\napp.include_router(item.router)')

    user_model = os.path.join(models_folder, 'user.py')
    with open(user_model, 'a') as f:
        f.write('\n\nclass User:\n    def __init__(self, id, name):\n        self.id = id\n        self.name = name')

    item_model = os.path.join(models_folder, 'item.py')
    with open(item_model, 'a') as f:
        f.write('\n\nclass Item:\n    def __init__(self, id, name):\n        self.id = id\n        self.name = name')

    test_main = os.path.join(tests_folder, 'test_main.py')
    with open(test_main, 'a') as f:
        f.write('\ndef test_get_users():\n    response = test_app().get("/api/users")\n    assert response.status_code == 200\n\ndef test_get_items():\n    response = test_app().get("/api/items")\n    assert response.status_code == 200')

    dashboard_route = os.path.join(routes_folder, 'dashboard.py')
    with open(dashboard_route, 'w') as f:
        f.write('from fastapi import APIRouter\nrouter = APIRouter()\n@router.get("/api/dashboard/tiles")\ndef get_dashboard_data():\n    return [{"id": 1, "name": "Tile1"}]')

    lms_route = os.path.join(routes_folder, 'lms.py')
    with open(lms_route, 'w') as f:
        f.write('from fastapi import APIRouter\nrouter = APIRouter()\n@router.post("/api/lms/leaves/apply")\ndef apply_for_leave():\n    return {"message": "Leave applied successfully"}\n@router.get("/leave/status")\ndef get_leave_status():\n    return {"status": "Pending"}\n@router.patch("/leave/approve/{id}")\ndef approve_leave(id):\n    return {"message": "Leave approved successfully"}')

    pods_route = os.path.join(routes_folder, 'pods.py')
    with open(pods_route, 'w') as f:
        f.write('from fastapi import APIRouter\nrouter = APIRouter()\n@router.get("/api/pods/{pod_id}/details")\ndef get_pod_details(pod_id):\n    return {"id": pod_id, "name": "Pod1"}\n@router.post("/api/pods/{pod_id}/recommend")\ndef recommend_employee(pod_id):\n    return {"message": "Employee recommended successfully"}')

    auth_route = os.path.join(routes_folder, 'auth.py')
    with open(auth_route, 'w') as f:
        f.write('from fastapi import APIRouter\nfrom fastapi.security import OAuth2PasswordBearer\nrouter = APIRouter()\noauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")\n@router.post("/api/auth/login")\ndef login():\n    return {"token": "access_token"}\n@router.get("/api/auth/user")\ndef get_user():\n    return {"id": 1, "name": "John"}')

    main_file = os.path.join(app_folder, 'main.py')
    with open(main_file, 'a') as f:
        f.write('\n\nfrom app.api.routes import dashboard, lms, pods, auth\n\napp.include_router(dashboard.router)\napp.include_router(lms.router)\napp.include_router(pods.router)\napp.include_router(auth.router)')

    test_dashboard = os.path.join(tests_folder, 'test_dashboard.py')
    with open(test_dashboard, 'w') as f:
        f.write('import pytest\nfrom app.main import app\n@pytest.fixture\ndef test_app():\n    return app\n\ndef test_get_dashboard_data():\n    response = test_app().get("/api/dashboard/tiles")\n    assert response.status_code == 200')

    test_lms = os.path.join(tests_folder, 'test_lms.py')
    with open(test_lms, 'w') as f:
        f.write('import pytest\nfrom app.main import app\n@pytest.fixture\ndef test_app():\n    return app\n\ndef test_apply_for_leave():\n    response = test_app().post("/api/lms/leaves/apply")\n    assert response.status_code == 200\n\ndef test_get_leave_status():\n    response = test_app().get("/leave/status")\n    assert response.status_code == 200\n\ndef test_approve_leave():\n    response = test_app().patch("/leave/approve/1")\n    assert response.status_code == 200')

    test_pods = os.path.join(tests_folder, 'test_pods.py')
    with open(test_pods, 'w') as f:
        f.write('import pytest\nfrom app.main import app\n@pytest.fixture\ndef test_app():\n    return app\n\ndef test_get_pod_details():\n    response = test_app().get("/api/pods/1/details")\n    assert response.status_code == 200\n\ndef test_recommend_employee():\n    response = test_app().post("/api/pods/1/recommend")\n    assert response.status_code == 200')

    test_auth = os.path.join(tests_folder, 'test_auth.py')
    with open(test_auth, 'w') as f:
        f.write('import pytest\nfrom app.main import app\n@pytest.fixture\ndef test_app():\n    return app\n\ndef test_login():\n    response = test_app().post("/api/auth/login")\n    assert response.status_code == 200\n\ndef test_get_user():\n    response = test_app().get("/api/auth/user")\n    assert response.status_code == 200')

generate_project_structure()