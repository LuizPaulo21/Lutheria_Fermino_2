from flask import Blueprint, render_template, request, session, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import hashlib, os, dotenv
from flask import current_app

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


@bp.route('/create_cliente', methods=['POST'])
def create_cliente():
    # Verifica se o método da requisição é POST e se os campos necessários foram preenchidos
    if request.method == 'POST':

        ejuridica = bool(request.form.get('tipoPessoaJuridica'))

        nome_completo = request.form.get('nomeCompleto')
        cpf = request.form.get('cpf')
        email = request.form.get('email')
        cnpj = request.form.get('cnpj')
        razao_social = request.form.get('razaoSocial')
        nome_fantasia = request.form.get('nomeFantasia')
        endereco = request.form.get('logradouro')
        cep = request.form.get('cep')
        bairro = request.form.get('bairro')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')

        cliente_data = {
                "nome": nome_completo,
                "cpf": cpf,
                "cnpj": cnpj,
                "razaoSocial": razao_social,
                "nomeFantasia": nome_fantasia,
                "email": email,
                "cnpj": cnpj,
                "endereco": endereco,
                "cep": cep,
                "bairro": bairro,  
                "cidade": cidade,
                "estado": estado, 
            }

        # Validação mínima na rota (o Caso de Uso fará a validação completa)
        if ejuridica:
            msg = "Nome e E-mail são campos obrigatórios."
            return render_template('cadastro_cliente.html', msg=msg)
        else:
            # Acessa o Caso de Uso
            use_case_key = 'use_case'
            if use_case_key not in current_app.extensions:
                msg = "Erro crítico: Configuração de casos de uso não encontrada."
                return render_template('cadastro_cliente.html', msg=msg)

            create_cliente_uc = current_app.extensions['use_case'].get('create_cliente')

            if not create_cliente_uc:
                msg = "Erro: Serviço de criação de cliente indisponível."
                return render_template('cadastro_cliente.html', msg=msg)
            
            try:
                novo_cliente = create_cliente_uc.execute(cliente_data)
                if novo_cliente:
                    msg = f"Cliente '{novo_cliente.get('nome', 'N/A')}' cadastrado com sucesso!"
                else:
                    msg = "Erro ao cadastrar cliente. Verifique os dados ou os logs do servidor."
            except ValueError as ve: # Captura erros de validação do Caso de Uso
                msg = f"Erro de validação: {ve}"
            except Exception as e:
                current_app.logger.error(f"Exceção em create_cliente (POST): {e}", exc_info=True)
                msg = "Ocorreu um erro inesperado ao processar sua solicitação."
    
    # Para o método GET (exibir o formulário) ou após o POST (para mostrar a msg)
    return render_template('cadastro_cliente.html', msg=msg)