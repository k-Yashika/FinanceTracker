from flask import Flask
from flask_sqlalchemy import SQLAlchemy as sqla
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'alabama_llama_mama'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
db = sqla(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes
from app.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
