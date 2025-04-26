import os
from flask import Flask

from. import funcoes
from. import routes

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

    return app
