import os
import dotenv
from flask import Flask

from repositories import clienteRepository
from repositories import produtoRepository
from repositories import pedidoRepository
from repositories import grupoRepository

from adapters.MongoAdapters import ClienteMongoAdapter
from adapters.MongoAdapters import ProdutoMongoAdapter
from adapters.MongoAdapters import PedidosMongoAdapter
from adapters.MongoAdapters import GrupoMongoAdapter

from. import funcoes
from. import routes

dotenv.load_dotenv()
login=os.getenv('user_MongoDB')
password=os.getenv('password_MongoDB')
uri = f"mongodb+srv://{login}:{password}@cluster0.25d5slc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def create_app(test_config=None):
    
    #Cria variável global Flask. __name__ é o nome do modulo python atual.
    #O segundo parametro, indica que os arquivos de configuração estão na pasta instance, que fica fora do pacote atual.
    app = Flask(__name__, instance_relative_config=True)

    #Define alguns parametros que o APP terá
    app.config.from_mapping(
        SECRET_KEY='dev',
        )

    if test_config is None:
        #Sobrescreve as configurações padrão por aquelas presentes no arquivo na pasta instance. Pode ser usado para definir uma SECRET_KEY verdadeira.
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Configurações de teste podem ser passadas, para diferir dos valores de desenvolvimento.
        app.config.from_mapping(test_config)

    try:
        #Para ter certeza que o diretório de instance exista
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Registra o blueprint criado (arquivo com rotas)
    app.register_blueprint(routes.bp)

    #Registra o blueprint criado (arquivo com funcoes)
    app.register_blueprint(funcoes.bp)

    #Inicializando os adaptadores para clientes
    try:
        # ClienteMongoAdapter que implementa a interface clienteRepository
        cliente_repository_instance: clienteRepository = ClienteMongoAdapter()
        print("ClienteMongoAdapter instanciado com sucesso.")
    except ConnectionError as e: # Supondo que seu adapter levante ConnectionError
        print(f"CRÍTICO: Falha ao conectar ao MongoDB na inicialização do adapter: {e}")
        cliente_repository_instance = None
    except Exception as e:
        print(f"CRÍTICO: Erro inesperado ao instanciar ClienteMongoAdapter: {e}")
        cliente_repository_instance = None

        #Inicializando os adaptadores para produtos
    try:
        # ClienteMongoAdapter que implementa a interface produtoRepository
        produto_repository_instance: produtoRepository = ProdutoMongoAdapter()
        print("ProdutoMongoAdapter instanciado com sucesso.")
    except ConnectionError as e: # Supondo que seu adapter levante ConnectionError
        print(f"CRÍTICO: Falha ao conectar ao MongoDB na inicialização do adapter: {e}")
        cliente_repository_instance = None
    except Exception as e:
        print(f"CRÍTICO: Erro inesperado ao instanciar ClienteMongoAdapter: {e}")
        cliente_repository_instance = None
    
    #Inicializando os adaptadores para pedidos
    try:
        # ClienteMongoAdapter que implementa a interface pedidoRepository
        pedido_repository_instance: pedidoRepository = PedidosMongoAdapter()
        print("PedidoMongoAdapter instanciado com sucesso.")
    except ConnectionError as e: # Supondo que seu adapter levante ConnectionError
        print(f"CRÍTICO: Falha ao conectar ao MongoDB na inicialização do adapter: {e}")
        cliente_repository_instance = None
    except Exception as e:
        print(f"CRÍTICO: Erro inesperado ao instanciar ClienteMongoAdapter: {e}")
        cliente_repository_instance = None

    #Inicializando os adaptadores para grupos de produtos
    try:
        # ClienteMongoAdapter que implementa a interface grupoProdutoRepository
        grupo_produto_repository_instance: grupoRepository = GrupoMongoAdapter()
        print("GrupoProdutoMongoAdapter instanciado com sucesso.")
    except ConnectionError as e: # Supondo que seu adapter levante ConnectionError
        print(f"CRÍTICO: Falha ao conectar ao MongoDB na inicialização do adapter: {e}")
        cliente_repository_instance = None
    except Exception as e:
        print(f"CRÍTICO: Erro inesperado ao instanciar ClienteMongoAdapter: {e}")
        cliente_repository_instance = None

    return app
