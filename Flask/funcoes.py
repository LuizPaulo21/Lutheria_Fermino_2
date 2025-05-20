from flask import Blueprint, render_template, request, session
import hashlib, os

bp = Blueprint("funcoes", __name__, url_prefix="/")

@bp.route('/login', methods=['POST'])
def login():

    # Aqui é verificado se o método da requisição é POST e se os compos necessários foram preenchidos. 
    # Em seguida, os valores dos campos são armazenados em variáveis.
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        usuario = request.form.get('username')
        senha = request.form.get('password')

    # Faz o hash da senha para evitar que a senha original seja exposta
    hash = senha + os.getenv('SECRET_KEY')
    hash = hashlib.sha1(hash.encode())
    senha = hash.hexdigest()

    # Checa se a conta existe no banco de dados


    # Busca um registro e retorna o resultado


    # Verificando se existe o usuario no banco de dados
    if usuario:
        # Dados da sessão
        session['loggedin'] = True
        session['id']= usuario[0]
        session['username']=usuario[1]

        # Redireciona ao inicio do sistema
        return render_template("base.html")
    else:
        msg = "Usuario ou senha incorretos!"

    return render_template('index.html', msg=msg)


