from flask import Blueprint, render_template 

errors_bp = Blueprint('errors', __name__, template_folder='templates')

@errors_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404
