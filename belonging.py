from flask import Blueprint, render_template, request, redirect
from models import Belonging
from database import db

bp_belonging = Blueprint('belonging', __name__, template_folder='templates')


@bp_belonging.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('belonging_create.html')
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')

        u = Belonging(name, email, password)
        db.session.add(u)
        db.session.commit()
        return '''
            <p>Belonging registered successfully</p>
            <br>
            <a href="/">Back to home</a>
        '''


@bp_belonging.route('/recovery')
def recovery():
    belonging = Belonging.query.all()
    return render_template('belonging_recovery.html', belonging=belonging)


@bp_belonging.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    u = Belonging.query.get(id)

    if request.method == 'GET':
        return render_template('belonging_update.html', u=u)

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        u.name = name
        u.email = email
        db.session.add(u)
        db.session.commit()
        return redirect('/belonging/recovery')


@bp_belonging.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    u = Belonging.query.get(id)

    if request.method == 'GET':
        return render_template('belonging_delete.html', u=u)

    if request.method == 'POST':
        db.session.delete(u)
        db.session.commit()
        return redirect('/belonging/recovery')

# -----------


bp_belonging = Blueprint('belonging', __name__, template_folder='templates')


@bp_belonging.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('belonging_create.html')
    if request.method == 'POST':
        category = request.form.get('category')
        description = request.form.get('description')
        brand = request.form.get('brand')
        count = request.form.get('count')
        price = request.form.get('price')

        u = Belonging(category, description, brand, count, price)
        db.session.add(u)
        db.session.commit()
        return '''
            <p>Belonging registered successfully</p>
            <br>
            <a href="/">Back to home</a>
        '''


@bp_belonging.route('/recovery')
def recovery():
    belonging = Belonging.query.all()
    return render_template('belonging_recovery.html', belonging=belonging)


@bp_belonging.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    u = Belonging.query.get(id)

    if request.method == 'GET':
        return render_template('belonging_update.html', u=u)

    if request.method == 'POST':
        category = request.form.get('category')
        description = request.form.get('description')
        brand = request.form.get('brand')
        count = request.form.get('count')
        price = request.form.get('price')
        u.category = category
        u.description = description
        u.brand = brand
        u.count = count
        u.price = price
        db.session.add(u)
        db.session.commit()
        return redirect('/belonging/recovery')


@bp_belonging.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    u = Belonging.query.get(id)

    if request.method == 'GET':
        return render_template('belonging_delete.html', u=u)

    if request.method == 'POST':
        db.session.delete(u)
        db.session.commit()
        return redirect('/belonging/recovery')
