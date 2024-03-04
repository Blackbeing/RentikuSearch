import unittest

from flask import jsonify, make_response, request

from RentikuSearch.api.v1.views import bp
from RentikuSearch.models import storage
from RentikuSearch.models.models import User


@bp.route("/user", methods=["GET", "POST"], strict_slashes=False)
def users():
    if request.method == "POST":
        data = request.get_json()
        if data:
            user = User(**data)
            user.save()
        return make_response(jsonify({}), 201)

    elif request.method == "GET":
        return_val = [user.to_dict() for user in storage.all(User)]
        return make_response(jsonify(return_val), 200)


@bp.route("/user/<id>", methods=["GET"], strict_slashes=False)
def get_user_by_id(id):
    return_val = storage.get(User, id)
    return make_response(jsonify(return_val), 200)


if __name__ == "__main__":
    unittest.main()
