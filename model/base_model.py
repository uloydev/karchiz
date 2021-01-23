from pymysql.connections import Connection
from database import DB

class BaseModel:
    _mysql: Connection
    _table: str

    def __init__(self):
        self._mysql = DB.connection()
    
    def insert(self, data: dict) -> bool:
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