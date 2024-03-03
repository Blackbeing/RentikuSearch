from config import get_config
from RentikuSearch.api.v1.app import create_app


def main():
    app = create_app(get_config())
    app.run()


if __name__ == "__main__":
    main()
