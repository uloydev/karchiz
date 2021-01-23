from .base_model import BaseModel
from flask import session
from entity import User

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

    def get_current_user(self) -> User:
        condition = f"username = '{session.get('username')}'"
        data = self.get_where(condition)
        return self.parse(data[0])

    def parse(self, data: dict) -> User:
        return User(**data)

    def parseList(self, data: list[dict]) -> list[User]:
        result = []
        for item in data:
            result.append(User(**item))
        return result