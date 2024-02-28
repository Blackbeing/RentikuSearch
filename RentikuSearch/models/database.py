from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from RentikuSearch.models.base_model import Base


class Database:

    def __init__(self, db_url=None):
        """
        Initializes Database class
        Arguments:
            db_url: Database db_url
             ex. "postgresql+psycopg2://johndoe:pass@localhost:5432/mydatabase"
        """

        self.db_url = db_url
        self.engine = create_engine(self.db_url)

    def reload(self):
        Base.metadata.create_all(self.engine)
        session_factory = sessionmaker(
            bind=self.engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.session = Session

    def disconnect(self):
        """
        Close db connection
        """
        if self.session:
            self.session.remove()

    def new(self, obj):
        self.session.add(obj)

    def save(self):
        self.session.commit()

    def delete(self, obj=None):
        if obj:
            self.session.remove(obj)
