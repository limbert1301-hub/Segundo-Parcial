from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.productos.models import Producto

bp_productos = Blueprint('bp_productos', __name__, template_folder='templates')

@bp_productos.route('/')
def index():
    productos = Producto.query.all()
    return render_template('producto/index.html', productos=productos)

@bp_productos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = float(request.form.get('precio'))
        stock = int(request.form.get('stock'))
        db.session.add(Producto(nombre=nombre, precio=precio, stock=stock))
        db.session.commit()
        return redirect(url_for('bp_productos.index'))
    return render_template('producto/create.html')

@bp_productos.route('/view/<int:id>')
def view(id):
    producto = Producto.query.get_or_404(id)
    return render_template('producto/view.html', producto=producto)

@bp_productos.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    producto = Producto.query.get_or_404(id)
    if request.method == 'POST':
        producto.nombre = request.form.get('nombre')
        producto.precio = float(request.form.get('precio'))
        producto.stock = int(request.form.get('stock'))
        db.session.commit()
        return redirect(url_for('bp_productos.index'))
    return render_template('producto/edit.html', producto=producto)

@bp_productos.route('/delete/<int:id>')
def delete(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('bp_productos.index'))