from lesson14.homework14.mycustomiterator import MyCustomIterator


class HumanIter(MyCustomIterator):
    def __init__(self, name: str, age: int):
        super().__init__()
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


if __name__ == "__main__":
    John = HumanIter("John", 23)
    Amanda = HumanIter("Amanda", 36)
    Jack = HumanIter("Jack", 73)
    Jack = HumanIter("Jack", 73)
    for pair in Jack:
        print(pair)

