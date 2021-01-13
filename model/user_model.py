from .base_model import BaseModel
from flask import session

class UserModel(BaseModel):
    def __init__(self):
        super(UserModel, self).__init__()
        self._table = 'user'

    def check_login(self, username: str, password: str) -> bool:
        __query = f'SELECT * FROM {self._table} WHERE username="{username}" AND password="{password}"'
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            if __cursor.fetchone():
                return True
        except Exception as e:
            print(e)
        return False

    def get_current_user(self) -> dict:
        condition = f"username = '{session.get('username')}'"
        user = self.get_where(condition)
        if not user:
            return {}
        return user[0]