import psycopg2

from lesson19.core.page_singleton import singleton


@singleton
class UserRepository:
    def __init__(self):
        self.__connection = psycopg2.connect(
            user="postgres",
            password="12345",
            host="127.0.0.1",
            port="5432",
            database="homework24"
        )
        self.__cursor = self.__connection.cursor()

    def get_all(self):
        self.__cursor.execute(
            "select * from users;"
        )
        return self.__cursor.fetchall()

    def delete_by_email(self, email: str):
        self.__cursor.execute(
            f"delete from users"
        )

    def update_by_id(self, id: int, name: str, email: str, age: int) -> None:
        self.__cursor.execute(
            f"update users set name = '{name}', "
            f"email = '{email}', "
            f"age = '{age}'"
            f"where id = '{id}';"
        )
        self.__connection.commit()

    def add_one(self, name: str, email: str, age: int) -> None:
        self.__cursor.execute(
            f"insert into users (name, email, age) values "
            f"('{name}', '{email}', '{age}')"
        )

    def __del__(self):
        if self.__connection:
            self.__cursor.close()
            self.__connection.close()


if __name__ == '__main__':
    user_repository = UserRepository()
    print(user_repository.get_all())
    user_repository.add_one('t', 't', 1)
    print(user_repository.get_all())
    # print(user_repository.get_all())