from interface import Interface

class Entity(Interface):
    
    def get_id(self) -> int:
        pass

    def set_id(self, id: int):
        pass