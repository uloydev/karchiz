from interface import Interface

class Entity(Interface):
    """interface dengan nama Entity dengan dua method yaitu setter dan getter id."""
    
    def get_id(self) -> int:
        pass

    def set_id(self, id: int):
        pass