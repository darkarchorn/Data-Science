from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, id, name, age, job):
        self._id = id
        self._name = name
        self._age = age
        self._job = job

    @abstractmethod
    def getProperty(self, propName):
        pass

    @abstractmethod
    def setProperty(self, propName, propValue):
        pass

class HumanImpl(Human):
    def getProperty(self, propName):
        return getattr(self, f"_{propName}", None)

    def setProperty(self, propName, propValue):
        if hasattr(self, f"_{propName}"):
            setattr(self, f"_{propName}", propValue)
            return True
        return False
