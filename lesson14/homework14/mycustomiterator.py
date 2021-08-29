class MyCustomIterator:

    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.__dict__):
            item = list(self.__dict__.items())[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration
