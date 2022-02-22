from enum import Enum
import uuid
import Util

class ItemStatus(Enum):
    NEW = 1
    USED = 2
    DAMAGED = 3
    BROKEN = 4

class ItemType(Enum):
    ITEM = 1
    LINGE = 2
    OUTIL = 3
    MACHINE = 4

class Item:
    id = None
    name = None
    type = None
    status = None

    def __init__(self, id: str=None, name: str="", type: ItemType=ItemType.ITEM, status: ItemStatus=ItemStatus.NEW):
        self.id = id or uuid.uuid4()
        self.name = name
        self.type = type or ItemType.ITEM
        self.status = status or ItemStatus.NEW
    
    def deserialize(line: str, separator: str=";"):
        a = line.split(separator)
        return Item(a[1], a[2], Util.str_to_instance(a[3]), Util.str_to_instance(a[4]))

    def serialize(self, separator: str=";"):
        return str(self.__class__.__name__) + separator + str(self.id) + separator + self.name + separator + str(self.type) + separator + str(self.status)

    def __repr__(self):
        return self.serialize()
    
    def __eq__(self, other):
        return str(self.id) == str(other.id)



if __name__ == "__main__":
    raise RuntimeError("Not meant to be run")
