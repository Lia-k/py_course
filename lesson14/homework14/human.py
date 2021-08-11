from lesson14.homework14.action import Action


class Human:
    def __init__(self, name: str, age: int, gender: str, action: str):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__action = Action(action)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @property
    def action(self) -> object:
        return self.__action


if __name__ == "__main__":
    John = Human("John", 23, "male", "video gaming")
    Amanda = Human("Amanda", 36, "female", "dancing")
    Jack = Human("Jack", 73, "male", "breathing")
    # pycharm offers me a tip of removing instances' call. If I do so,
    # it then offers me to add call
    John.action()
    Amanda.action()
    Jack.action()
