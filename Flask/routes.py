from flask import Blueprint, render_template

bp = Blueprint("routes", __name__, url_prefix="/")

#Rota da página inicial
@bp.route('/hello')
def hello():
    return 'Hello, World!'