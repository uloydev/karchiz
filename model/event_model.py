from .base_model import BaseModel
from entity import Event

class EventModel(BaseModel):
    def __init__(self):
        super(EventModel, self).__init__()
        self._table = 'event'

    def get_category(self, category_id: int) -> list:
        # membuat kondisi where
        condition = f'category_id = {category_id}'
        # menjalankan query dan mengemabalikan hasilnya
        return self.get_where(condition)

    def parse(self, data: dict) -> Event:
        return Event(**data)

    def parseList(self, data: list[dict]) -> list[Event]:
        result = []
        for item in data:
            result.append(Event(**item))
        return result