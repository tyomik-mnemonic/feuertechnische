from abc import ABCMeta, abstractmethod
from collections import namedtuple

class Equipment(metaclass=ABCMeta):
    #TODO: добавить универсальнные геттеры сеттеры в абстрактный класс
    @abstractmethod
    def name()->str:
        raise NotImplementedError
    
    @abstractmethod
    def type_tags()->list:
        raise NotImplementedError

    @abstractmethod
    def description()->str:
        raise NotImplementedError

    @abstractmethod
    def tool_property()->dict or namedtuple:
        raise NotImplementedError

    


