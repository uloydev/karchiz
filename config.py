from pymysql.cursors import DictCursor


class Config():
    host: str
    user: str
    password: str
    db: str
    cursorclass: DictCursor

    def __init__(self):
        """Fungsi Constructor dari class Config.
        
        digunakan untuk set akun database mysql
        """
        self.host = 'localhost'
        self.user = 'root'
        self.password ='passwordnya'
        self.db = 'karchiz'
        self.cursorclass = DictCursor

    def get(self) -> dict:
        """Fungsi get config.

        Returns:
            dict: dictionary gabungan dari semua variabel / properti dari class config
        """
        return self.__dict__