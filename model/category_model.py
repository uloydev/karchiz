from .base_model import BaseModel
from entity import Category

class CategoryModel(BaseModel):
    def __init__(self):
        """Fungsi constructor dari class CategoryModel yang digunakan untuk memanggil constructor parent class
        dan mengisi properti _tabel dengan nama tabel.
        """
        super(CategoryModel, self).__init__()
        self._table = 'category'

    def parse(self, data: dict) -> Category:
        """Fungsi parse digunakan untuk mengubah data hasil query yang berupa dictionary menjadi object.

        Args:
            data (dict): data hasil query berupa dictionary

        Returns:
            Category: object dari class Category
        """
        return Category(**data)

    def parseList(self, data: list[dict]) -> list[Category]:
        """Fungsi parseList digunakan untuk mengubah data hasil query yang berupa list dari dictionary menjadi list dari object.

        Args:
            data (list[dict]): list / array dari hasil query

        Returns:
            list[Category]: list / array dari object class Category
        """
        result = []
        for item in data:
            result.append(Category(**item))
        return result