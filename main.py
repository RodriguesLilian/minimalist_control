from database import db
from flask import Flask, render_template
from flask_migrate import Migrate
from users import bp_users

app = Flask(__name__)

connection = 'sqlite:///mysqlite.sqlite'

app.config['SECRET_KEY'] = 'mixel'
app.config['SQLALCHEMY_DATABASE_URI'] = connection
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(bp_users, url_prefix='/users')

migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template('home.html')


app.run(host='0.0.0.0', port=81)
