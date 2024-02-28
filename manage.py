import os

from dotenv import load_dotenv

from config import get_config
from RentikuSearch.api.v1.app import create_app


def main():
    load_dotenv()
    flask_env = os.getenv("FLASK_ENV")
    app = create_app(get_config(flask_env))
    app.run()


if __name__ == "__main__":
    main()
