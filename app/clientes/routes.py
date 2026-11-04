from flask import Blueprint, render_template, request, redirect, url_for
from app import db  # o desde app.app dependiendo de tu importación actual
from app.clientes.models import Cliente

bp_clientes = Blueprint('bp_clientes', __name__, template_folder='templates')

@bp_clientes.route('/')
def index():
    clientes = Cliente.query.all()
    return render_template('cliente/index.html', clientes=clientes)

@bp_clientes.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')
        db.session.add(Cliente(nombre=nombre, telefono=telefono))
        db.session.commit()
        return redirect(url_for('bp_clientes.index'))
    return render_template('cliente/create.html')

@bp_clientes.route('/view/<int:id>')
def view(id):
    cliente = Cliente.query.get_or_404(id)
    return render_template('cliente/view.html', cliente=cliente)

@bp_clientes.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.nombre = request.form.get('nombre')
        cliente.telefono = request.form.get('telefono')
        db.session.commit()
        return redirect(url_for('bp_clientes.index'))
    return render_template('cliente/edit.html', cliente=cliente)

@bp_clientes.route('/delete/<int:id>')
def delete(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('bp_clientes.index'))