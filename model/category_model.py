from .base_model import BaseModel
from entity import Category

class CategoryModel(BaseModel):
    def __init__(self):
        super(CategoryModel, self).__init__()
        self._table = 'category'

    def parse(self, data: dict) -> Category:
        return Category(**data)

    def parseList(self, data: list[dict]) -> list[Category]:
        result = []
        for item in data:
            result.append(Category(**item))
        return result