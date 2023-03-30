from market import app
from flask import render_template,redirect, url_for, flash, get_flashed_messages,request
from market import Item, User, db
from market.forms import RegistrationForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user
@app.route('/')
def root():
    return render_template('home.html')
@app.route('/land/<param>', methods=['GET','POST'])
def landing(param):
    param=len('FIC')
    return render_template('landingpage.html',param=param)
@app.route('/market', methods=['GET','POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if purchase_form.validate_on_submit():
        #note that the purchase_form is a dict with keys 'submit' which has also has html attribute
        #print(purchase_form['submit']) returns<input id="submit" name="submit" type="submit" value="Purchase!">
        #and we'll copy this to the top of our submit button for altering
        #let us import request from flask to be able to het the particular item clicked on for purchase
        #print(request.form.get('purchase_item')) iPhone 14
        purchased_item = request.form.get('purchased_item')
        purchased_item_object = Item.query.filter_by(name=purchased_item).first()
        if purchased_item_object:
            #let us assign this Item to the current_user by importing it from FlaskLogin
            
            if current_user.budget > purchased_item_object.price:
                current_user.budget -= purchased_item_object.price
                purchased_item_object.owner = current_user.id
                db.session.commit()
                flash(f'You have successfully purchased {purchased_item}',category='success')
            else:
                flash(f'You do not have a sufficient balance to purchase this Item, Kindly increase your budget', category= 'danger')
                
    #moving forward, we want to display item that does yet have an owner on the market
    #that technically means items that arent yet purchased  
    #let us move from  items = Item.query.all()         
    items = Item.query.filter_by(owner=None)
    
    
    """[{"id":1,"name":"phone","barcode":"8886","Price":1200},{
        "id":2,"name":"Keyboard","barcode":"8886","Price":5
        },{"id":3,"name":"Laptop","barcode":"8886","price":700
            
        }]"""
    return render_template('market.html', items = items, purchase_form = purchase_form)
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
        login_user(user_to_create)
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
    flash("You have been logged out!", category='info')
    return redirect(url_for("root"))
