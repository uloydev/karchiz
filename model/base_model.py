from pymysql.connections import Connection
from database import DB

class BaseModel:
    _mysql: Connection
    _table: str

    def __init__(self):
        """Fungsi constructor untuk class BaseModal dan akan mengisi properti _mysql dengan koneksi database."""
        self._mysql = DB.connection()
    
    def insert(self, data: dict) -> bool:
        """Fungsi insert digunakan untuk menginput data kedalam suatu tabel.

        Args:
            data (dict): dictionary data berupa nama kolom (key) dan value 

        Returns:
            bool: true jika berhasil melakukan query ke database
        """
        # get columns names and values
        __columns = data.keys()
        __values = [ f'"{val}"' for val in data.values()]
        # build query
        __query = f'INSERT INTO {self._table}({",".join(__columns)}) VALUES ({",".join(__values)})'
        # try to send query to database
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_all(self) -> list:
        """Fungsi get_all digunakan  untuk mengambil semua data di dalam suatu tabel.

        Returns:
            list: list / array dari hasil query
        """
        # build query
        __query = f'SELECT * FROM {self._table}'
        # try to send query to database
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return __cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def get(self) -> dict:
        """Fungsi get digunakan untuk mengambil satu baris data di suatu tabel.

        Returns:
            dict: dictionary dari kolom (key) dan value
        """
        # build query
        __query = f'SELECT * FROM {self._table}'
        # try to send query to database
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return __cursor.fetchone()
        except Exception as e:
            print(e)
            return {}

    def get_where(self, condition: str) -> list:
        """Fungsi get_where digunakan untuk mengambil semua data di suatu tabel dengan kondisi tertentu.

        Args:
            condition (str): where statement

        Returns:
            list: list / array dari hasil query
        """
        # build query
        __query = f'SELECT * FROM {self._table} WHERE {condition}'
        # try to send query to database
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return __cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def update(self, data: dict, _id: int) -> bool:
        """Fungsi update digunakan untuk memperbarui suatu data yang ada di suatu tabel.

        Args:
            data (dict): dictionary data berupa nama kolom (key) dan value
            _id (int): id dari data yang akan diupdate

        Returns:
            bool: true jika berhasil melakukan query ke database
        """
        # menyiapkan array dari value baru
        __items = [ f'{key}="{data[key]}"' for key in data]
        # build query
        __query = f'UPDATE {self._table} SET {",".join(__items)} WHERE id = {_id}'
        # try to send query to database
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, _id: int) -> bool:
        """Fungsi delete digunakan untuk menghapus suatu data yang ada di suatu tabel.

        Args:
            _id (int): id dari data yang ingin dihapus

        Returns:
            bool: true jika berhasil melakukan query ke database
        """
        # build query
        __query = f'DELETE FROM {self._table} WHERE id = {_id}'
        # try to send query to database
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return True
        except Exception as e:
            print(e)
            return False