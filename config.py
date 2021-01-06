import pymysql.cursors

class Config():
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password ='passwordnya'
        self.db = 'karchiz'
        self.cursorclass = pymysql.cursors.DictCursor

    def get(self):
        return self.__dict__