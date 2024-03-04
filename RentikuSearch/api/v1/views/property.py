from flask import jsonify, make_response, request

from RentikuSearch.api.v1.views import bp
from RentikuSearch.models import storage
from RentikuSearch.models.models import Property


@bp.route("/property/<id>", methods=["GET"], strict_slashes=False)
def get_property_by_id(id):
    return_val = storage.get(Property, id)
    return make_response(jsonify(return_val.to_dict()), 200)


@bp.route("/property", methods=["GET", "POST"], strict_slashes=False)
def property():
    if request.method == "POST":
        data = request.get_json()
        if data:
            property = Property(**data)
            property.save()
        return make_response(jsonify({}), 201)

    elif request.method == "GET":
        return_val = [
            property.to_dict() for property in storage.all(Property)
        ]
        return make_response(jsonify(return_val), 200)
