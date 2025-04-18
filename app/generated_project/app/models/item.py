from pydantic import BaseModel
class Item(BaseModel):
    id: int
    name: str

class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name