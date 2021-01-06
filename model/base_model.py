class BaseModel:
    def __init__(self, mysql):
        self._mysql = mysql
        self._table = ''
    
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