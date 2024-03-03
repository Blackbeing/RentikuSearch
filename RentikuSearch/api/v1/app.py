from flask import Flask

from config import BaseConfig
from RentikuSearch.api.v1.views import bp
from RentikuSearch.models import storage


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
    app.register_blueprint(bp)

    @app.route("/test/")
    def test_page():
        return "<h1>Flask Factory Pattern</h1>"

    @app.teardown_request
    def close_session(req):
        storage.disconnect()

    return app


if __name__ == "__main__":
    from config import get_config

    app = create_app(get_config())
    app.run()
