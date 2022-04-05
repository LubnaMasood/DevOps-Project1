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
    return "Added your order into the system!"

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