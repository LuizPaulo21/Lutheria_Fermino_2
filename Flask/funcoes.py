from flask import Blueprint, render_template, request, session
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import hashlib, os, dotenv

bp = Blueprint("funcoes", __name__, url_prefix="/")

dotenv.load_dotenv()
login=os.getenv('user_MongoDB')
password=os.getenv('password_MongoDB')
uri = f"mongodb+srv://{login}:{password}@cluster0.25d5slc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

@bp.route('/login', methods=['POST'])
def login():

    # Aqui é verificado se o método da requisição é POST e se os compos necessários foram preenchidos. 
    # Em seguida, os valores dos campos são armazenados em variáveis.
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        usuario = request.form.get('username')
        senha = request.form.get('password')

    # Faz o hash da senha para evitar que a senha original seja exposta
    hash = senha + os.getenv('SECRETKEY')
    hash = hashlib.sha1(hash.encode())
    senha = hash.hexdigest()

    # Cria uma conexão ao MongoDB
    db = "LutheriaFermino2" # Nome do banco de dados
    collection = "usuarios" # Nome da coleção de clientes
    # Cria um novo cliente MongoDB e se conecta com o servidor
    client = MongoClient(uri, server_api=ServerApi('1'))
    collection = client[db][collection]

    # Busca um registro e retorna o resultado
    usuario = collection.find_one({
        "usuario": usuario,
        "senha": senha
    })

    #Convertendo o id do usuario para string
    if usuario:
        usuario['_id'] = str(usuario['_id'])

    # Verificando se existe o usuario no banco de dados
    if usuario:
        # Dados da sessão
        session['loggedin'] = True
        session['id']= usuario['_id']
        session['username']=usuario['usuario']

        # Redireciona ao inicio do sistema
        return render_template("inicio.html")
    else:
        msg = "Usuario ou senha incorretos!"

    return render_template('inicio.html', msg=msg)


