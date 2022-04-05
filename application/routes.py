from application import app, db
from application.models import Customer, Customer_order
from application.forms import SignUpForm, ViewOrderForm, UpdateForm
from flask import Flask, render_template, url_for, request
from sqlalchemy.orm import session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, EmailField
from werkzeug.utils import redirect
from wtforms.validators import data_required


@app.route('/')
@app.route('/homepage')
def home():
    return render_template(homepage.html)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
         email = form.email.data
         phone_number = form.phone_number.data
         username = form.username.data
         password = form.password.data
         customer = Customer(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,username=username,password=password)
         db.session.add(customer)
         db.session.commit()

    return redirect(url_for('home'))
    else:
        return render_template('signup.html', form = form)


@app.route('/vieworder', methods = ['GET', 'POST'])
def vieworder():
    view_order = Customer_order(name="There are no orders to view!")
    db.session.add(view_order)
    db.session.commit()
    return "Place an order to view your orders!"

@app.route('/update', methods = ['GET', 'POST'])
def update():
    update = Customer(name="Update your information!")
    db.session.add(update)
    db.session.commit()
    return "Your information has been updated!"

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    delete = Customer(name="Delete your information!")
    db.session.add(delete)
    db.session.commit()
    return "Your information has been deleted!"