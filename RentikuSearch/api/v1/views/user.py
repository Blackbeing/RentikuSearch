import unittest

from flask import jsonify, make_response, request

from RentikuSearch.api.v1.views import bp
from RentikuSearch.models.models import User


@bp.route("/user", methods=["GET", "POST"], strict_slashes=False)
def user():
    if request.method == "POST":
        data = request.get_json()
        if data:
            user = User(**data)
            user.save()
        return make_response(jsonify({}), 201)

    elif request.method == "GET":
        return make_response(jsonify({}), 200)


if __name__ == "__main__":
    unittest.main()
