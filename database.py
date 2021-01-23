import pymysql
from pymysql.connections import Connection
from config import Config

class DB:
    @staticmethod
    def connection() -> Connection:
        """Fungsi statis connection untuk membuat koneksi dengan database.

        Returns:
            Connection: berisi koneksi database
        """
        __config = Config().get()
        return pymysql.connect(**__config)
