# Создайте итератор принимающий последовательность и умеющий перебирать
# значения по заданному диапазону. CustomIterator(sequence, start_index,
# end_index)
# end_index item включительно
class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    @property
    def sequence(self):
        return self.__sequence

    @property
    def start_index(self):
        return self.__start_index

    @property
    def end_index(self):
        return self.end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < len(self.__sequence) > self.__end_index \
                and self.__start_index != self.__end_index + 1:
            item = self.__sequence[self.__start_index]
            self.__start_index += 1
            return item
        else:
            raise StopIteration


if __name__ == "__main__":
    custom_iterator = CustomIterator([1, 2, 3, 4, 5, 6], 3, 3)
    iterator = iter(custom_iterator)
    for i in custom_iterator:
        print(i)
