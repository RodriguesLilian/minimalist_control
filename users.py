from flask import Blueprint, render_template, request, redirect
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


@bp_users.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    u = User.query.get(id)

    if request.method == 'GET':
        return render_template('users_update.html', u=u)

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        u.name = name
        u.email = email
        db.session.add(u)
        db.session.commit()
        return redirect('/users/recovery')


@bp_users.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    u = User.query.get(id)

    if request.method == 'GET':
        return render_template('users_delete.html', u=u)

    if request.method == 'POST':
        db.session.delete(u)
        db.session.commit()
        return redirect('/users/recovery')
