from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancias globales de extensiones
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configuración de SQLite y claves de sesión
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///techbol.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'techbol_secret_key'

    # Inicializar extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar y registrar los Blueprints con sus prefijos exactos
    from app.clientes.routes import bp_clientes
    from app.productos.routes import bp_productos
    from app.pedidos.routes import bp_pedidos

    app.register_blueprint(bp_clientes, url_prefix='/clientes')
    app.register_blueprint(bp_productos, url_prefix='/productos')
    app.register_blueprint(bp_pedidos, url_prefix='/pedidos')

    return app