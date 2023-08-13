from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá mundo"

# error handler
@app.errorhandler(404)
def not_found(error):
    return "Página não encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)