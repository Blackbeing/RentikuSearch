from sqlalchemy import create_engine
# create url from env
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

from RentikuSearch.config import settings


class Database:
    __session = None
    __engine = None

    def __init__(self):
        self.username = settings.DB_USERNAME
        self.password = settings.DB_PASSWORD
        self.host = settings.DB_HOST
        self.port = settings.DB_PORT
        self.database = settings.DB_NAME
        self.drivername = settings.DB_DRIVERNAME

        db_url = URL.create(
            drivername=self.drivername,
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )

        self.__engine = create_engine(db_url)
        self.__session_factory = sessionmaker(
            autocommit=False, autoflush=False, bind=self.__engine
        )
        if settings.TESTING:
            self.drop_tables()
            self.init_db()

    @property
    def session(self):
        return self.__session_factory

    @property
    def engine(self):
        return self.__engine()

    def init_db(self):
        Base.metadata.create_all(self.__engine)

    def drop_tables(self):
        Base.metadata.drop_all(self.__engine)


Base = declarative_base()


def get_db():
    db = Database().session
    try:
        yield db
    finally:
        db.close()
