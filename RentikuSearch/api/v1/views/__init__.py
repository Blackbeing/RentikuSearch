from flask import Blueprint

bp: Blueprint = Blueprint("api_views", __name__, url_prefix="/api/v1")

from RentikuSearch.api.v1.views.index import *
from RentikuSearch.api.v1.views.user import *
