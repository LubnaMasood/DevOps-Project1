from application import app, db
from application.models import Customer, Customer_order
from application.forms import CustomerForm, Customer_orderForm
from flask import render_template, url_for, request, redirect


@app.route('/')
@app.route('/homepage')
def homepage():
    all_customers = Customer.query.all()
    all_orders = Customer_order.query.all()
    return render_template('homepage.html', all_customers=all_customers, all_orders=all_orders)

@app.route('/create_customer', methods = ['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_customer = Customer(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, phone_number=form.phone_number.data, username=form.username.data, password=form.password.data)
            db.session.add(new_customer)
            db.session.commit()
        return redirect(url_for("create_customer"))


@app.route('/create', methods = ['GET', 'POST'])
def create():
    form = CustomerForm()
    if request.method == "POST":
        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            phone_number = form.phone_number.data
            username = form.username.data
            password = form.password.data
            customer = Customer(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, phone_number=form.phone_number.data, username=form.username.data, password=form.password.data)
            db.session.add(customer)
            db.session.commit()
            return redirect(url_for('homepage', message="New Customer Added!"))
        else:
            return render_template('add.html', title="Create Customer", form = form)

    else:
        return render_template('add.html', title="Create Customer", form = form)

@app.route('/addorder', methods=["GET", "POST"])
def addorder():
    form = Customer_orderForm()
    all_orders = Customer_order.query.all()
    if request.method == "POST":
        if form.validate_on_submit():
            new_order = Customer_order(id=form.id.data, date_placed=form.date_placed.data, order_status=form.order_status.data)
            db.session.add(new_order)
            db.session.commit()
            return  redirect(url_for("homepage"))
        else:
            return render_template('add_order.html', title="Add Order", form = form)
    else:
            return render_template('add_order.html', title="Add Order", form = form)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = CustomerForm()
    customer = Customer.query.filter_by(id=id).first()
    if request.method == "POST":
        customer.first_name = form.first_name.data
        customer.last_name = form.last_name.data
        customer.email = form.email.data
        customer.phone_number = form.phone_number.data
        customer.username = form.username.data
        customer.password = form.password.data 
        db.session.commit()
        return  redirect(url_for("homepage"))
    else:
        return render_template("update.html", form=form, title="Update Customer", customer=customer)

@app.route("/updateorder/<int:id>", methods=["GET", "POST"])
def updateorder(id):
    form = Customer_orderForm()
    order = Customer_order.query.filter_by(id=id).first()
    if request.method == "POST":
        order.date_placed = form.date_placed.data
        order.order_status = form.order_status.data
        db.session.commit()
        return  redirect(url_for("homepage"))
    else:
        return render_template("updateorder.html", form=form, title="Update Order", order=order)

@app.route("/delete/<int:id>")
def delete(id):
    order = Customer_order.query.filter_by(id=id).first()
    if delete:
        db.session.delete(order)
        db.session.commit()
        return redirect(url_for('homepage'))
    else: 
        return render_template('homepage.html', message="Order Deleted!")

@app.route("/deletecustomer/<int:id>")
def deletecustomer(id):
    customer = Customer.query.filter_by(id=id).first()
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return redirect(url_for("homepage"))
    else:
        return render_template("homepage.html", message="Customer Deleted!")
