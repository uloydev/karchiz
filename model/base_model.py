from pymysql.connections import Connection
from database import DB

class BaseModel:
    def __init__(self):
        self._mysql = DB.connection()
        self._table : str
    
    def insert(self, data: dict) -> bool:
        __columns = data.keys()
        __values = [ f'"{val}"' for val in data.values()]
        __query = f'INSERT INTO {self._table}({",".join(__columns)}) VALUES ({",".join(__values)})'
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_all(self) -> list:
        __query = f'SELECT * FROM {self._table}'
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return __cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def get(self) -> dict:
        __query = f'SELECT * FROM {self._table}'
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return __cursor.fetchone()
        except Exception as e:
            print(e)
            return {}

    def get_where(self, condition: str) -> list:
        __query = f'SELECT * FROM {self._table} WHERE {condition}'
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return __cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def update(self, data: dict, _id: int) -> bool:
        __items = [ f'{key}="{data[key]}"' for key in data]
        __query = f'UPDATE {self._table} SET {",".join(__items)} WHERE id = {_id}'
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, _id: int) -> bool:
        __query = f'DELETE FROM {self._table} WHERE id = {_id}'
        try:
            __cursor = self._mysql.cursor()
            __cursor.execute(__query)
            self._mysql.commit()
            return True
        except Exception as e:
            print(e)
            return False