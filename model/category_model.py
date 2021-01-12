from .base_model import BaseModel

class CategoryModel(BaseModel):
    def __init__(self):
        super(CategoryModel, self).__init__()
        self._table = 'category'