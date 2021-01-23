from flask import session
from .base_model import BaseModel
from .user_model import UserModel
from entity import Order

class OrderModel(BaseModel):
    def __init__(self):
        super(OrderModel, self).__init__()
        self._table = 'orders'

    def get_user_orders(self) -> list[Order]:
        user = UserModel().get_current_user()
        orders = self.get_where(f'user_id={user["id"]}')
        return self.parseList(orders)

    def parse(self, data: dict) -> Order:
        return Order(**data)

    def parseList(self, data: list[dict]) -> list[Order]:
        result = []
        for item in data:
            result.append(Order(**item))
        return result