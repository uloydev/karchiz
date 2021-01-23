from interface import implements
from .entity import Entity
from .ticket import Ticket
from .event import Event


class Order(implements(Entity)):
    __id: int
    __ticket_id: int
    __user_id: int
    __order_time: str
    __ticket: Ticket
    __event: Event

    def __init__(self, id:int, user_id:int, ticket_id:int, order_time:str):
        self.__id = id
        self.__ticket_id = ticket_id
        self.__user_id = user_id
        self.__order_time = order_time

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id
        
    def get_ticket_id(self) -> int:
        return self.__ticket_id

    def set_ticket_id(self, ticket_id: int):
        self.__ticket_id = ticket_id
    
    def get_user_id(self) -> int:
        return self.__user_id

    def set_user_id(self, user_id: int):
        self.__user_id = user_id

    def get_order_time(self) -> str:
        return self.__order_time

    def set_order_time(self, order_time: str):
        self.__order_time = order_time

    def get_ticket(self) -> Ticket:
        return self.__ticket

    def set_ticket(self, ticket: Ticket):
        self.__ticket = ticket

    def get_event(self) -> Event:
        return self.__event

    def set_event(self, event: Event):
        self.__event = event
