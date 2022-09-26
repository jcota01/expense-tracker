from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    expenses = db.relationship('Expense')
    income = db.relationship('Income')

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, db.ForeignKey(User.username))
    title = db.Column(db.Text, nullable=False, default=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, title, price, category):
        self.username = username
        self.title = title
        self.price = price
        self.category = category
        self.created = datetime.now()


class Income(db.Model):
    __tablename__ = 'income'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, db.ForeignKey(User.username))
    income = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, income):
        self.username = username
        self.income = income
        self.date = datetime.now()


def init_db():
    db.drop_all()
    db.create_all()
    new_user = User(username="test_name", password="hello")
    new_expense = Expense(username="test_name", title="test_title", price=5.59, category="Entertainment")
    db.session.add(new_user)
    db.session.add(new_expense)
    db.session.commit()
    print("done")
