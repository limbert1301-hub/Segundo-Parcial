from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.pedidos.models import Pedido
from app.clientes.models import Cliente
from app.productos.models import Producto

bp_pedidos = Blueprint('bp_pedidos', __name__, template_folder='templates')

@bp_pedidos.route('/')
def index():
    pedidos = Pedido.query.all()
    return render_template('pedido/index.html', pedidos=pedidos)

@bp_pedidos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('pedido/create.html', clientes=Cliente.query.all(), productos=Producto.query.all())
    elif request.method == 'POST':
        db.session.add(Pedido(
            fecha=request.form.get('fecha'),
            monto=float(request.form.get('monto')),
            cliente_id=request.form.get('cliente_id'),
            producto_id=request.form.get('producto_id')
        ))
        db.session.commit()
        return redirect(url_for('bp_pedidos.index'))

@bp_pedidos.route('/view/<int:id>')
def view(id):
    pedido = Pedido.query.get_or_404(id)
    return render_template('pedido/view.html', pedido=pedido)

@bp_pedidos.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    pedido = Pedido.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('pedido/edit.html', pedido=pedido, clientes=Cliente.query.all(), productos=Producto.query.all())
    elif request.method == 'POST':
        pedido.fecha = request.form.get('fecha')
        pedido.monto = float(request.form.get('monto'))
        pedido.cliente_id = request.form.get('cliente_id')
        pedido.producto_id = request.form.get('producto_id')
        db.session.commit()
        return redirect(url_for('bp_pedidos.index'))

@bp_pedidos.route('/delete/<int:id>')
def delete(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('bp_pedidos.index'))