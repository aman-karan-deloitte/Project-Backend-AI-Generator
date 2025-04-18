from fastapi import APIRouter
router = APIRouter()

class UserRoute:
    def __init__(self, app):
        self.app = app

    def get_users(self):
        return [{"id": 1, "name": "John"}]