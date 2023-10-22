from database import db
from flask import Flask, render_template
from flask_migrate import Migrate
from belonging import bp_belonging

app = Flask(__name__)

connection = 'sqlite:///mysqlite.sqlite'

app.config['SECRET_KEY'] = 'mixel'
app.config['SQLALCHEMY_DATABASE_URI'] = connection
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(bp_belonging, url_prefix='/belonging')

migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template('belonging_home.html')
