from flask.cli import FlaskGroup

from config import get_config
from RentikuSearch.web_flask import create_app

app = create_app(get_config())

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
