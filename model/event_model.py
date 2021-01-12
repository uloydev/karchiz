from .base_model import BaseModel

class EventModel(BaseModel):
    def __init__(self):
        super(EventModel, self).__init__()
        self._table = 'event'

    def get_category(self, category_id: int) -> list:
        condition = f'category_id = {category_id}'
        return self.get_where(condition)