import pymysql
from pymysql.connections import Connection
from config import Config

class DB:
    @staticmethod
    def connection() -> Connection:
        __config = Config().get()
        return pymysql.connect(**__config)
