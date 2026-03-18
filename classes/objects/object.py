from abc import ABC, abstractmethod

class Object(ABC):

    @abstractmethod
    def hit(self, ray, t_min, t_max):
        pass

    @abstractmethod
    def getColor(self, hitPoint):
        pass

    @abstractmethod
    def getNormal(self, hitPoint):
        pass
