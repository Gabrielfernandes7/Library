from flask import Flask
from database import db
from flask_migrate import Migrate

# Swagger
from flask_restx import Resource, Api
from werkzeug.middleware.proxy_fix import ProxyFix

# Blueprints
from app.users import bp_users
from app.books import bp_books
from app.rent import bp_rents

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='API de Exemplo',
    description='Uma simples API de exemplo com Flask e Swagger')
ns = api.namespace('todos', description='TODO operations')

conection_with_database = 'sqlite:///database.sqlite.db'

# configs
app.config['SECRET_KEY'] = 'minha-chave'
app.config['SQLALCHEMY_DATABASE_URI'] = conection_with_database
app.config['SQLALCHEMY_TRACKMODIFICATIONS']= False

# Register Blueprints
app.register_blueprint(bp_users, url_prefix='/users')
app.register_blueprint(bp_books, url_prefix='/books')
app.register_blueprint(bp_rents, url_prefix='/rents')

db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def index():
    return "Página principal"

@ns.response(200, "successful")
@ns.route('/hello', endpoint='todo_ep')
class TodoSimple(Resource):
    def get(self):
        return "hello"

# error handler
@app.errorhandler(404)
def not_found(error):
    return "Página não encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)