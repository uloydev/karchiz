from .base_model import BaseModel

class UserModel(BaseModel):
    def __init__(self, mysql):
        super(UserModel, self).__init__(mysql)
        self._table = 'user'