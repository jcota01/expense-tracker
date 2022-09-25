import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense-tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


if __name__ == '__main__':
    my_host = "127.0.0.1"
    app.secret_key = os.urandom(16)

    # BLUEPRINTS
    from users.views import users_blueprint
    from expenses.views import expenses_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(expenses_blueprint)

    app.run(host=my_host, debug=True)
