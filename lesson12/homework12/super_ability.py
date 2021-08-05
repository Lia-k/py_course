from abc import ABC, abstractmethod


class SuperAbility(ABC):

    @abstractmethod
    def increase_strength(self, parameter):
        """
        Describes increase strength parameter sub-classes
        """
        pass

    @abstractmethod
    def use_ability(self, parameter):
        """
        Describe the way the ability is used for the sub-classes
        """
        pass
