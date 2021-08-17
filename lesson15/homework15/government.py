from __future__ import annotations

from lesson15.homework15.government_singleton import singleton


@singleton
class Government:
    def __init__(self,
                 form: str,
                 economic_system: str,
                 autonomy: str,
                 principles: str):
        self.__form = form
        self.__economic_system = economic_system
        self.__autonomy = autonomy
        self.__principles = principles

    @property
    def form(self):
        return self.__form

    @property
    def economic_system(self):
        return self.__economic_system

    @property
    def autonomy(self):
        return self.__autonomy

    @property
    def principles(self):
        return self.__principles

