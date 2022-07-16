from flask import Blueprint

loader_blueprint = Blueprint('loader', __name__, template_folder='templates', static_folder='static')