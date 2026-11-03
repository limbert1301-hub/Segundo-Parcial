from flask import Blueprint, render_template

bp_pedidos = Blueprint('bp_pedidos', __name__, template_folder='templates')

@bp_pedidos.route('/')
def index():
    return "Módulo de Pedidos activo"