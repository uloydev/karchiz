from flask import session
from .base_model import BaseModel
from .user_model import UserModel

class OrderModel(BaseModel):
    def __init__(self):
        super(OrderModel, self).__init__()
        self._table = 'orders'

    def get_user_orders(self):
        user = UserModel().get_where(f'username = "{session["username"]}"')[0]
        return self.get_where(f'user_id={user["id"]}')