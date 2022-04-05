from application import app, db
from application.models import Customer, Customer_order
from flask import render_template, url_for, request


@app.route('/')
@app.route('/homepage')
def home():
    return 'Welcome to the home page!'


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    new_customer = Customer(name="New Customer")
    db.session.add(new_customer)
    db.session.commit()
    return "Added new customer to the database!"

@app.route('/placeorder', methods = ['GET', 'POST'])
def placeorder():
    new_order = Customer_order(name="Order Placed!")
    db.session.add(new_order)
    db.session.commit()
    return "Added new customer order to the database!"