from database import db
from flask import Flask
from flask_migrate import Migrate
from usuarios import bp_usuarios

app = Flask(__name__)

conexao = 'sqlite:///meubanco.sqlite'

app.config['SECRET_KEY'] = 'mixel'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(bp_usuarios, url_prefix='/usuarios')

migrate = Migrate(app, db)


@app.route("/")
def index():
    return "<p> Hello, from Flask </p>"


app.run(host='0.0.0.0', port=81)
