# У вас есть магазин. Хочу что бы ваш магазин давал мне необходимый товар по
# приметам. Market класс должен содержать метод возвращающий товар.
# Соответственно могут быть следующие товары: Apple, Banana, Celery,
# Strawberry. Каждый из этих продуктов имеет общего родителя Product который
# абстрактный класс. (фабричный метод)
from lesson15.homework15.market import Market

if __name__ == "__main__":
    apple = Market.get_product('apple')
    banana = Market.get_product('banana')
    celery = Market.get_product('celery')
    strawberry = Market.get_product('strawberry')
    test = Market.get_product("test")
    print(apple)
    print(banana)
    print(celery)
    print(strawberry)
    print(test)
