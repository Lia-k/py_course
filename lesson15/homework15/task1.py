# Описать объект на ваше усмотрение. Экземпляр объекта может быть лишь один
# в системе. Хочу увидеть паттерн синглтон но статическое поле инстанс хочу
# видеть приватным.
from lesson15.homework15.government import Government

if __name__ == '__main__':
    government = Government("monarchy",
                            "feudalism",
                            "empire",
                            "The king is dead, long live the king!")
    government_1 = Government("test", "test", "test", "test")
    print(government.form)
    print(government_1.form)
