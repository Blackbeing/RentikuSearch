import psycopg2
from sqlalchemy import URL, create_engine


class Database:
    def __init__(
        self, host=None, dbname=None, user=None, password=None, db_url=None
    ):
        """
        Initializes Database class
        Arguments:
            host: db host address
            dbname: Name of database
            user: User
            password: password
            db_url: Database db_url
             ex. "postgresql+psycopg2://johndoe:pass@localhost:5432/mydatabase"
        """

        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.db_url = db_url

    def connect(self):
        """
        Create connection to database, create sqlalchemy engine
        """
        try:
            if self.db_url:
                self.conn = psycopg2.connect(self.db_url)
                self.engine = create_engine(self.db_url)
            else:
                self.conn = psycopg2.connect(
                    host=self.host,
                    dbname=self.dbname,
                    user=self.user,
                    password=self.password,
                )
                url_object = URL(
                    "postgresql+psycopg2",
                    host=self.host,
                    database=self.dbname,
                    username=self.user,
                    password=self.password,
                    port=5432,
                    query={},
                )
                self.engine = create_engine(url_object)
        except Exception as e:
            print(e)

        self.cursor = self.conn.cursor()

    def disconnect(self):
        """
        Close db connection
        """
        if self.conn:
            self.conn.close()

    def execute(self, query):
        """
        Execute db query and commit
        Arguments:
            query: SQL query
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
