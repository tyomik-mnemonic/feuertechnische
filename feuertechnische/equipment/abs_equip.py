from abc import ABCMeta, abstractmethod

class Equipment(metaclass=ABCMeta):
    @abstractmethod
    def kingdom_name():
        raise NotImplementedError


class FireEquipment(Equipment):
    def __init__(self):
        self.kingdom_name = "Feuertechnische stueken"

    def kingdom_name(self):
        return self.kingdom_name

