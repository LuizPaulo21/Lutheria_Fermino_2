from flask import Blueprint, render_template

bp = Blueprint("routes", __name__, url_prefix="/")

#Rota da página login
@bp.route('/')
@bp.route('/index')
def hello():
    return render_template("login.html")

#Rota da página inicial
@bp.route('/inicio.html')
def inicio():
    return render_template("inicio.html")

################################
# Seção de páginas de cadastro #
################################

#Rota para a pagina de cadastro de cliente
@bp.route('/cadastro_cliente.html')
def cadastro_cliente():
    return render_template("cadastro_cliente.html")

#Rota para Cadastro de pedidos
@bp.route('/cadastro_pedido.html')
def cadastro_pedido():
    return render_template("cadastro_pedido.html")

#Rota para Cadastro de produtos
@bp.route('/cadastro_produto.html')
def cadastro_produto():
    return render_template("cadastro_produto.html")

#Rota para Cadastro de Grupos de produtos
@bp.route('/cadastro_grupo.html')   
def cadastro_grupo_produto():
    return render_template("cadastro_grupo.html")

#################################
# Seção de páginas de alteração #
#################################