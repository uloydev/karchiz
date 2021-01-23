from interface import implements
from .entity import Entity


class People(implements(Entity)):
    __id: int
    __avatar: str

    def __init__(self, id:int, avatar:str):
        self.__id = id
        self.__avatar = avatar

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_avatar(self) -> str:
        return self.__avatar

    def set_avatar(self, avatar: str):
        self.__avatar = avatar
        