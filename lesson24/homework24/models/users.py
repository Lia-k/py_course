from sqlalchemy import VARCHAR, Integer, Column
from sqlalchemy.orm import declarative_base
from sqlalchemy import Sequence


Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, nullable=False, unique=True,
                primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    email = Column(VARCHAR(25), nullable=False, unique=True)
    age = Column(Integer, nullable=False)

    def __str__(self):
        return f"\n{self.id}\n{self.name}\n{self.age}\n{self.email}"
