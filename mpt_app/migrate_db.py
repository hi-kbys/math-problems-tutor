from sqlalchemy import create_engine

from mpt_app.models.problem import Base

DB_URL = "mysql+mysqlconnector://root@db:3306/mpt?charset=utf8"
engine = create_engine(DB_URL, echo=True)

def reset_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    reset_db()