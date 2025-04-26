from flask import Blueprint, render_template, request


bp = Blueprint("funcoes", __name__, url_prefix="/")

@bp.route('/login', methods=['POST'])
def login():

    # Aqui é verificado se o método da requisição é POST e se os compos necessários foram preenchidos. 
    # Em seguida, os valores dos campos são armazenados em variáveis.
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        usuario = request.form.get('username')
        senha = request.form.get('password')

    return render_template("inicio.html")