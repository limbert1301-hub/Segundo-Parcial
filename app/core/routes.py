from flask import Blueprint, render_template

# Definir el Blueprint para core
bp_core = Blueprint('bp_core', __name__, template_folder='templates')

@bp_core.route('/')
def index():
    return render_template('core/index.html')