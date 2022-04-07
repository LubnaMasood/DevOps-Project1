from application import app, db
from flask import render_template, url_for, request, redirect
from application.models import Customer, Customer_order
from application.forms import CustomerForm, Customer_orderForm


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html', message="Homepage")

@app.route('/add_customer', methods = ['GET', 'POST'])
def add_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        new_customer = Customer(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, phone_number=form.phone_number.data, username=form.username.data, password=form.password.data)
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('add_customer', message="New Customer Added!" ))
    else:
        return render_template('add_customer.html', form=form)

@app.route('/delete_order/<int:order_id>', methods=['GET', 'POST'])
def delete_order(order_id):
    delete_order = db.session.query(Customer).filter_by(order_id=order_id).first()
    if deleted_order:
        db.session.delete(delete_order)
        db.session.commit()
        return redirect(url_for('vieworder'))

@app.route('/delete_customer/<int:customer_id>', methods=['GET', 'POST'])
def delete_customer(customer_id):
    delete_customer = db.session.query(Customer).filter_by(customer_id=customer_id).first()
    if customer:
        db.session.delete(delete_customer)
        db.session.commit()
        return redirect(url_for('viewcustomer'))

@app.route('/update_customer/<int:customer_id>', methods =['GET', 'POST'])
def update_customer(customer_id):
    update_customer = db.session.query(Customer).filter_by(customer_id=customer_id).first()
    if update_customer:
            update_customer.first_name = request.form ['First name']
            update_customer.last_name = request.form ['Last name']
            update_customer.email = request.form ['Email']
            update_customer.phone_number = request.form ['Phone Number']
            update_customer.username = request.form ['Username']
            update_customer.password = request.form ['Password']
            db.session.commit()
        return redirect(url_for('viewcustomer', message="Customer Info Updated!"))
    else:
        return render_template('homepage.html', form=form, customer_id=customer_id)


@app.route('/update_order/<int:order_id>', methods =['GET', 'POST'])
def update_order(order_id):
    update_order = db.session.query(Customer_order).filter_by(order_id=order_id).first()
    if request.method == 'POST':
        order = Customer_order.query.filter_by(order_id=order_id).first()
        if update_order:
            update_customer.order_id = request.form ['Order ID']
            update_customer.username = request.form ['Username']
            update_customer.password = request.form ['Password']
            db.session.commit()
        return redirect(url_for('vieworder', message="Customer Info Updated!"))
    else:
        return render_template('homepage.html', form=form, order_id=order_id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')