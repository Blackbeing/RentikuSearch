from flask import jsonify

from RentikuSearch.api.v1.views import bp


@bp.route("/status", strict_slashes=False)
def setatus():
    return jsonify({"status": "Alive"})
