from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config["SECRET_KEY"]='bdfbcdc502722bc560583a98'
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ="login_page"
login_manager.login_message_category="info"
login_manager.login_message= "Please login before continuing to the Market page"
from market.models import Item,User
