from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from config import get_config

Base = declarative_base()


class Database:
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes Database class
        Arguments:
            db_url: Database db_url
             ex. "postgresql+psycopg2://johndoe:pass@localhost:5432/mydatabase"
        """
        self.config = get_config()
        self.db_url = self.config.DATABASE_URL
        self.__engine = create_engine(self.db_url)

        if self.config.TESTING:
            self.init_db()

    def init_db(self):
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session

    def disconnect(self):
        """
        Close db connection
        """
        self.__session.remove()

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.remove(obj)

    def all(self, klass):
        return self.__session.query(klass).all()

    def get(self, klass, id):
        return self.__session.query(klass).filter(klass.id == id).first()

    def drop_db(self):
        Base.metadata.drop_all(self.__engine)

    def session(self):
        return self.__session
