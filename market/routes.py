from market import app
from flask import render_template,redirect, url_for, flash, get_flashed_messages
from market import Item, User, db
from market.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user
@app.route('/home')
def root():
    return render_template('home.html')
@app.route('/land/<param>', methods=['GET','POST'])
def landing(param):
    param=len('FIC')
    return render_template('landingpage.html',param=param)
@app.route('/market')
def market_page():
    items= Item.query.all()
    
    """[{"id":1,"name":"phone","barcode":"8886","Price":1200},{
        "id":2,"name":"Keyboard","barcode":"8886","Price":5
        },{"id":3,"name":"Laptop","barcode":"8886","price":700
            
        }]"""
    return render_template('market.html', items=items)
@app.route("/register", methods=['GET','POST'])
def register_page(): 
    form = RegistrationForm()
    if form.validate_on_submit():
        user_to_create= User(username=form.username.data.strip(),
                             email_address=form.email_address.data.strip(), password=form.password1.data)
        
        #with app.app_context():
            #db.create_all()
        db.session.add(user_to_create)
        db.session.commit()
        flash(f'Hello {user_to_create.username}, Your  registration was successfully!', category="success")
        return redirect(url_for('market_page'))
    
    if form.errors !={}: #if there are no  errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error creating a user: {err_msg}',category='danger')
        
    return render_template('register.html', form=form)    
@app.route('/login',methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and  attempted_user.check_password_correlation(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'You are successfully logged in as: {attempted_user.username}!', category='success')
            return redirect(url_for('market_page'))
        else:
            flash(f'Username and Password do not match, please try again!', category='danger')
    return render_template('login.html',form=form)
@app.route('/logout', methods=['GET','POST'])
def logout_page():
    logout_user()
    flash("You have been logged out!",category='info')
    return redirect(url_for("root"))
