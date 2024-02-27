from flask import Flask

from config import BaseConfig


def create_app(config_class=BaseConfig):
    """
    Create and configure an instance of the Flask application
    Arguments:
        config_class: Configuration class
    Returns:
        app: Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config_class())

    # test url
    @app.route("/test/")
    def test_page():
        return "<h1>Flask Factory Pattern</h1>"

    return app
