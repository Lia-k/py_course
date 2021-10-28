from sqlalchemy import MetaData

from lesson24.homework24.models.users import Users
from lesson24.homework24.session import session


class UsersRepository:
    def __init__(self):
        self.__session = session

    def get_all(self):
        for user in self.__session.query(Users).all():
            print(user)

    def delete_one_by_email(self, delete_email: str):
        obj = self.__session.query(Users).filter_by(email=delete_email).one()
        self.__session.delete(obj)
        self.__session.commit()

    def update_one_by_id(self,
                         modify_id: int,
                         modify_name: str,
                         modify_email: str,
                         modify_age: int):
        self.__session.query(Users)\
            .filter_by(id=modify_id)\
            .update({
                    Users.name: modify_name,
                    Users.email: modify_email,
                    Users.age: modify_age
                    })
        self.__session.commit()

    def add_one(self, add_name: str, add_email: str, add_age: int):
        self.__session.add(Users(name=add_name, email=add_email, age=add_age))
        self.__session.commit()


if __name__ == '__main__':
    users_repository = UsersRepository()
    users_repository.add_one('test', 'test', 11)
    users_repository.get_all()
    users_repository.update_one_by_id(1, 'update test', 'update test email', 1)
    users_repository.get_all()
    users_repository.delete_one_by_email('update test email')
    users_repository.get_all()
