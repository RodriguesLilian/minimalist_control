from flask import Blueprint, render_template, request
from models import User
from database import db

bp_users = Blueprint('users', __name__, template_folder='templates')


@bp_users.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('users_create.html')
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        # return 'Dados recebidos'

        u = User(name, email, password)
        db.session.add(u)
        db.session.commit()
        return '''
            <p>User registered successfully</p>
            <br>
            <a href="/">Back to home</a>
        '''


@bp_users.route('/recovery')
def recovery():
    users = User.query.all()
    return render_template('users_recovery.html', users=users)
