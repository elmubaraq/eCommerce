from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config["SECRET_KEY"]='bdfbcdc502722bc560583a98'
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
from market.models import Item,User
