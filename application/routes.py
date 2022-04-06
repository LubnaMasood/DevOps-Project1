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
        return render_template('signup.html', form=form)


@app.route('/vieworder', methods = ['GET', 'POST'])
def vieworder():
    return render_template('vieworder.html')

@app.route('/update', methods = ['GET', 'POST'])
def update():
    form = UpdateForm()
    customer = Customer.query.get(customer_id)
    if form.validate_on_submit():
        email = form.new_email.data
        if email:
            customer.email=email
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('update.html', form=form)


@app.route('/delete')
def delete(username=None):
    if username == None:
        return "No Username Found!"
    else: 
        customer=Customer.query.get(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return render_template('homepage.html)
