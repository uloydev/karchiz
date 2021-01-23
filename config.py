from pymysql.cursors import DictCursor


class Config():
    host: str
    user: str
    password: str
    db: str
    cursorclass: DictCursor

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password ='passwordnya'
        self.db = 'karchiz'
        self.cursorclass = DictCursor

    def get(self) -> dict:
        return self.__dict__