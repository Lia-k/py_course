class Action:
    def __init__(self, name: str):
        self.__name = name

    @property
    def action_name(self):
        return self.__name

    def __call__(self):
        print(f"I am fond of {self.__name}.")
