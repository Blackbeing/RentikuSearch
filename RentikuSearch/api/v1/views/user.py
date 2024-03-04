from flask import jsonify, make_response, request

from RentikuSearch.api.v1.views import bp
from RentikuSearch.models import storage
from RentikuSearch.models.models import User


@bp.route("/user/<id>", methods=["GET"], strict_slashes=False)
def get_user_by_id(id):
    return_val = storage.get(User, id).to_dict()
    return make_response(jsonify(return_val), 200)


@bp.route("/user", methods=["GET", "POST"], strict_slashes=False)
def users():
    if request.method == "POST":
        data = request.get_json()
        if data:
            user = User(**data)
            user.save()
        return make_response(jsonify(user.to_dict()), 201)

    elif request.method == "GET":
        return_val = [user.to_dict() for user in storage.all(User)]
        return make_response(jsonify(return_val), 200)
