from fastapi import APIRouter
router = APIRouter()

class ItemRoute:
    def __init__(self, app):
        self.app = app

    def get_items(self):
        return [{"id": 1, "name": "Item1"}]