from flask import Blueprint

bp_clientes = Blueprint('bp_clientes', __name__, template_folder='templates')

@bp_clientes.route('/')
def index():
    return "Módulo de Clientes funcionando"