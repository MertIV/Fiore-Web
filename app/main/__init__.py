
from flask import Blueprint

bp = Blueprint('bp', __name__, url_prefix='/<lang_code>')


from app.main import routes