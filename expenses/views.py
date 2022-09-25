from flask import Blueprint, render_template, flash, redirect, url_for
from expenses.forms import ExpenseForm
from app import db
from models import Expense

expenses_blueprint = Blueprint('expenses', __name__, template_folder='templates')


@expenses_blueprint.route('/', methods=['GET', 'POST'])
def expenses():
    form = ExpenseForm()

    if form.validate_on_submit():
        new_expense = Expense(username="1", title=form.title.data, price=form.price.data, category=form.category.data)
        db.session.add(new_expense)
        db.session.commit()

    return render_template('index.html', form=form)
