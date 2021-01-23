from interface import implements
from .entity import Entity
from .ticket import Ticket

class Event(implements(Entity)):
    __id: int
    __title: str
    __schedule: str
    __category_id: int
    __description: str
    __tickets: list[Ticket]

    def __init__(self, id:int, title:str, schedule:str, category_id:int, description:str):
        self.__id = id
        self.__title = title
        self.__schedule = schedule
        self.__category_id = category_id
        self.__description = description

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def get_schedule(self) -> str:
        return self.__schedule

    def set_schedule(self, schedule: str):
        self.__schedule = schedule
        
    def get_category_id(self) -> int:
        return self.__category_id

    def set_category_id(self, category_id: int):
        self.__category_id = category_id

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str):
        self.__description = description

    def get_tickets(self) -> list[Ticket]:
        return self.__tickets

    def set_tickets(self, tickets: list[Ticket]):
        self.__tickets = tickets

