from flask import Blueprint, render_template

bp_usuarios = Blueprint('usuarios', __name__, template_folder='tempaltes')


@bp_usuarios.route('/create')
def create():
    return render_template('usuarios_create.html')
