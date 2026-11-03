from flask import Blueprint, render_template

bp_productos = Blueprint('bp_productos', __name__, template_folder='templates')

@bp_productos.route('/')
def index():
    return "Módulo de Productos activo"