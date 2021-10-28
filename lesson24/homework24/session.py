from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine("postgresql://postgres:12345@localhost/homework24")

__session = sessionmaker(engine)
session: Session = __session()
