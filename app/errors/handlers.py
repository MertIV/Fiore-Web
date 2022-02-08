from flask import render_template
from app.errors import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/page-404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/page-500.html'), 500
