from .base_model import BaseModel
from entity import Event

class EventModel(BaseModel):
    def __init__(self):
        """Fungsi constructor dari class EventModel yang digunakan untuk memanggil constructor parent class
        dan mengisi properti _tabel dengan nama tabel.
        """
        super(EventModel, self).__init__()
        self._table = 'event'

    def get_category(self, category_id: int) -> list:
        """Fungsi get_category digunakan untuk mengambil data event dengan kategory tertentu.

        Args:
            category_id (int): id kategori

        Returns:
            list: list dari data hasil query
        """
        # membuat kondisi where
        condition = f'category_id = {category_id}'
        # menjalankan query dan mengemabalikan hasilnya
        return self.get_where(condition)

    def parse(self, data: dict) -> Event:
        """Fungsi parse digunakan untuk mengubah data hasil query yang berupa dictionary menjadi object.

        Args:
            data (dict): data hasil query berupa dictionary

        Returns:
            Event: object dari class Event
        """
        return Event(**data)

    def parseList(self, data: list[dict]) -> list[Event]:
        """Fungsi parseList digunakan untuk mengubah data hasil query yang berupa list dari dictionary menjadi list dari object.

        Args:
            data (list[dict]): list / array dari hasil query

        Returns:
            list[Event]: list / array dari object class Event
        """
        result = []
        for item in data:
            result.append(Event(**item))
        return result