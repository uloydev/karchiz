from .people import People


class User(People):
    __id: int
    __avatar: str
    __username: str
    __password: str
    __age: int
    __gender: str

    def __init__(self, id: int, avatar: str, username: str, password: str, age: int, gender: str):
        self.__id = id
        self.__avatar = avatar
        self.__username = username
        self.__password = password
        self.__age = age
        self.__gender = gender

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_avatar(self) -> str:
        return self.__avatar

    def set_avatar(self, avatar: str):
        self.__avatar = avatar

    def get_username(self) -> str:
        return self.__username

    def set_username(self, username: str):
        self.__username = username

    def get_password(self) -> str:
        return self.__password

    def set_password(self, password: str):
        self.__password = password

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        self.__age = age

    def get_gender(self) -> str:
        return self.__gender

    def set_gender(self, gender: str):
        self.__gender = gender
