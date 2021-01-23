from interface import implements
from .entity import Entity


class Ticket(implements(Entity)):
    __id: int
    __event_id: int
    __type: str
    __price: int

    def __init__(self, id:int, event_id:int, type:str, price:int):
        self.__id = id
        self.__event_id = event_id
        self.__type = type
        self.__price = price

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id
        
    def get_event_id(self) -> int:
        return self.__event_id

    def set_event_id(self, event_id: int):
        self.__event_id = event_id

    def get_type(self) -> str:
        return self.__type

    def set_type(self, type: str):
        self.__type = type

    def get_price(self) -> int:
        return self.__price

    def set_price(self, price: int):
        self.__price = price
