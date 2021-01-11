import pymysql
from pymysql.connections import Connection
from config import Config

class DB:
    __config = Config().get()

    @classmethod
    def connection(cls) -> Connection:
        return pymysql.connect(**cls.__config)