from .base_model import BaseModel
from flask import session
from entity import User

class UserModel(BaseModel):
    def __init__(self):
        """Fungsi constructor dari class UserModel yang digunakan untuk memanggil constructor parent class
        dan mengisi properti _tabel dengan nama tabel.
        """
        super(UserModel, self).__init__()
        self._table = 'user'

    def check_login(self, username: str, password: str) -> bool:
        """Fungsi ini digunakan untuk pengecekan user ada di database atau tidak

        Args:
            username (str): username yang akan dicek
            password (str): password yang akan di cek

        Returns:
            bool: true jika user ditemukan
        """
        # build sql query
        __query = f'SELECT * FROM {self._table} WHERE username="{username}" AND password="{password}"'
        # try to send query to database
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
        """Fungsi get_current_user digunakan untuk mengambil data user yang sedang login saat ini.

        Returns:
            User: object dari class User
        """
        condition = f"username = '{session.get('username')}'"
        data = self.get_where(condition)
        return self.parse(data[0])

    def parse(self, data: dict) -> User:
        """Fungsi parse digunakan untuk mengubah data hasil query yang berupa dictionary menjadi object.

        Args:
            data (dict): data hasil query berupa dictionary

        Returns:
            User: object dari class User
        """
        return User(**data)

    def parseList(self, data: list[dict]) -> list[User]:
        """Fungsi parseList digunakan untuk mengubah data hasil query yang berupa list dari dictionary menjadi list dari object.

        Args:
            data (list[dict]): list / array dari hasil query

        Returns:
            list[User]: list / array dari object class User
        """
        result = []
        for item in data:
            result.append(User(**item))
        return result