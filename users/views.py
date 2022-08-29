from flask import Blueprint, render_template
from users.forms import RegisterForm, LoginForm

users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)

    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)

    return render_template('login.html', form=form)
