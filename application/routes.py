from application import app, db
from flask import render_template, url_for, request, redirect
from application.models import Customer, Customer_order
from application.forms import add_customer, delete_customer, delete_order, update_customer, update_order, vieworder

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html', message="Homepage")

@app.route('/add_customer', methods = ['GET', 'POST'])
def add_customer():
    form = add_customer()
    if form.validate_on_submit():
        new_customer = Customer(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, phone_number=form.phone_number.data, username=form.username.data, password=form.password.data)
        db.session.add(new_customer)
        db.session.commit()
        return render_template('homepage.html', message="New Customer Added!")
    else:
        return render_template('add_customer.html', form=form)

@app.route('/delete_customer', methods=['GET', 'POST'])
def delete_customer(customer):
    form = delete_customer()
    if order == None:
        return "No Customer Found!"
    else: 
        customer=Customer.query.get(customer_id)
        db.session.delete(delete_customer)
        db.session.commit()
    return render_template('delete_customer.html')

@app.route('/delete_order', methods=['GET', 'POST'])
def delete_order(order):
    form = delete_order()
    if order == None:
        return "No Order Found!"
    else: 
        order=Customer_order.query.get(order_id)
        db.session.delete(delete_order)
        db.session.commit()
    return render_template('delete_order.html')
    
@app.route('/update_customer', methods = ['GET', 'POST'])
def update_customer():
    form = update_customer()
    customer = Customer.query.get(customer_id)
    if form.validate_on_submit():
        email = form.new_email.data
        if email:
            customer.email=email
        db.session.commit()
        return redirect(url_for('homepage.html', message="Customer Info Updated!"))
    else:
        return render_template('update_customer.html', form=form)

@app.route('/update_order', methods = ['GET', 'POST'])
def update_order():
    form = update_order()
    if form.validate_on_submit():
        order = form.new_order.data
        return redirect(url_for('homepage.html', message="Order Info Updated!"))
    else:
        return render_template('update_order.html', form=form)

