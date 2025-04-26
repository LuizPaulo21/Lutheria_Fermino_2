from flask import Blueprint, render_template

bp = Blueprint("routes", __name__, url_prefix="/")

#Rota da página login
@bp.route('/')
@bp.route('/index')
def hello():
    return render_template("login.html")

#Rota da página inicial
@bp.route('/inicio')
def inicio():
    return render_template("inicio.html")