from flask import Flask
from database import db
from flask_migrate import Migrate

# Blueprints
from app.users import bp_users
from app.books import bp_books
from app.rent import bp_rents

app = Flask(__name__)

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

# error handler
@app.errorhandler(404)
def not_found(error):
    return "Página não encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)