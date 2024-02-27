from sqlalchemy import create_engine


class Database:
    def __init__(self, db_url=None):
        """
        Initializes Database class
        Arguments:
            db_url: Database db_url
             ex. "postgresql+psycopg2://johndoe:pass@localhost:5432/mydatabase"
        """

        self.db_url = db_url

    def connect(self):
        """
        Create connection to database, create sqlalchemy engine
        """
        try:
            self.engine = create_engine(self.db_url)
            self.conn = self.engine.connect()
        except Exception as e:
            print(e)

    def disconnect(self):
        """
        Close db connection
        """
        if self.conn:
            self.conn.close()
