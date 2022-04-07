from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from application.models import Customer, Customer_order

class CustomerForm(FlaskForm):
    first_name = StringField("First Name: ", validators=[DataRequired()])
    last_name = StringField("Last Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    phone_number = IntegerField("Phone Number: ", validators=[DataRequired()])
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField('Sign Up!')

class Customer_orderForm(FlaskForm):
    customer_id = IntegerField("Customer ID: ", validators=[DataRequired()])
    date_placed = DateField("Date Placed: ", validators=[DataRequired()])
    order_status = StringField("Order Status: ", validators=[DataRequired()])
