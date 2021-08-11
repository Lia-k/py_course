class Action:
    def __init__(self, action_name: str):
        self.__action_name = action_name

    @property
    def action_name(self):
        return self.__action_name

    def __call__(self):
        print(f"I am fond of {self.__action_name}")
