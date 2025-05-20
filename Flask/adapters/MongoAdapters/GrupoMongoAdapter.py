import os, dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId #Para converter para ObjectId

dotenv.load_dotenv()

# Carregar as variáveis de ambiente do arquivo .env
login=os.getenv('user_MongoDB')
password=os.getenv('password_MongoDB')
uri = f"mongodb+srv://{login}:{password}@cluster0.25d5slc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

class PedidoMongoAdapter:
    def __init__(self, str = "LutheriaFermino2"):

        self.db_name = str # Nome dob banco de dados
        self.collection_name = "clientes" # Nome da coleção de clientes

        # Cria um novo cliente MongoDB e se conecta com o servidor
        client = MongoClient(uri, server_api=ServerApi('1'))

        # COnfirmando a conexão
        try:
            client.admin.command('ping')
            return print("Conexão estabelecida com sucesso")
        except Exception as e:
            return print(e)
        
