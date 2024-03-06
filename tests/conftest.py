import os

import pytest


@pytest.fixture(autouse=True)
def set_testing_env():
    os.environ["FLASK_ENV"] = "testing"
    yield
    del os.environ["FLASK_ENV"]
