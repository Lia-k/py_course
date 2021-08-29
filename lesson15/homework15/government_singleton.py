from typing import Type


def singleton(_class: Type):

    def inner(*args):
        if not hasattr(_class, f"_{_class.__name__}__instance"):
            setattr(_class, f"_{_class.__name__}__instance", _class(*args))
        return getattr(_class, f"_{_class.__name__}__instance")

    return inner


# almost right but instance not in private attributes -3 points
