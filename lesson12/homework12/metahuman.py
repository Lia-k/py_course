from lesson12.homework12.human import Human
from lesson12.homework12.super_ability import SuperAbility


class MetaHuman(Human, SuperAbility):
    def __init__(self, name: str, age: int, strength: int, weight: int,
                 height: float, chronic_illness: str, heart_beats: bool,
                 origin: str, additional_strength: int, fly: bool,
                 immortality: bool, ability: str, weakness: str,
                 additional_speed: int, super_hero_name: str, disguise: str):
        self._name = name
        self._age = age
        self._strength = strength
        self._weight = weight
        self._height = height
        self.__chronic_illness = chronic_illness
        self._heart_beats = heart_beats
        self._origin = origin
        self._additional_strength = additional_strength
        self._fly = fly
        self._immortality = immortality
        self._ability = ability
        self._weakness = weakness
        self._additional_speed = additional_speed
        self.__super_hero_name = super_hero_name
        self.__disguise = disguise

    @property
    def super_hero_name(self):
        return self.__super_hero_name

    @property
    def disguise(self):
        return self.__disguise

    def hide_identity(self):
        return f"I am {self.__disguise} to hide identity"

    def live(self):
        if self._heart_beats:
            return "I am still alive"

    def work(self, job: str):
        if self._age < 16:
            return f"I am too young to work. But I would like to be {job}"
        elif self._age > 70:
            return f"I am too old for this s**t. I used to be {job}"
        else:
            return f"I am {job}"

    def run(self, speed: int):
        return self._additional_speed + speed

    def die(self):
        if not self._immortality:
            return "I am dying"
        else:
            return "Oh, no! Can not kill me!"

    def increase_strength(self, increase_strength: int):
        return self._strength + increase_strength

    def use_ability(self, purpose: str):
        return f"I am using {self._ability} to {purpose}"



