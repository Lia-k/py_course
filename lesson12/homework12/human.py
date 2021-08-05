from abc import ABC, abstractmethod


class Human(ABC):

    @abstractmethod
    def live(self):
        """
        Describes a live method for the sub-classes
        """
        pass

    @abstractmethod
    def work(self, parameter):
        """
        Describes the work method for the sub-classes
        """
        pass

    @abstractmethod
    def run(self, parameter):
        """
        Describes run method for sub-classes
        """
        pass

    @abstractmethod
    def die(self):
        """
        Describes die method for sub-classes
        """
        pass



