from flask import session
from .base_model import BaseModel
from .user_model import UserModel
from entity import Order

class OrderModel(BaseModel):
    def __init__(self):
        """Fungsi constructor dari class OrderModel yang digunakan untuk memanggil constructor parent class
        dan mengisi properti _tabel dengan nama tabel.
        """
        super(OrderModel, self).__init__()
        self._table = 'orders'

    def get_user_orders(self) -> list[Order]:
        """Fungsi get_user_orders digunakan untuk mengambil semua order yang dimiliki user yang sedang login saat ini.

        Returns:
            list[Order]: list / array dari object class Order
        """
        user = UserModel().get_current_user()
        orders = self.get_where(f'user_id={user["id"]}')
        return self.parseList(orders)

    def parse(self, data: dict) -> Order:
        """Fungsi parse digunakan untuk mengubah data hasil query yang berupa dictionary menjadi object.

        Args:
            data (dict): data hasil query berupa dictionary

        Returns:
            Order: object dari class Order
        """
        return Order(**data)

    def parseList(self, data: list[dict]) -> list[Order]:
        """Fungsi parseList digunakan untuk mengubah data hasil query yang berupa list dari dictionary menjadi list dari object.

        Args:
            data (list[dict]): list / array dari hasil query

        Returns:
            list[Order]: list / array dari object class Order
        """
        result = []
        for item in data:
            result.append(Order(**item))
        return result