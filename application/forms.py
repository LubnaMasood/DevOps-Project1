from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, EmailField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from application.models import Customer, Customer_order

class add_customer(FlaskForm):
    first_name = StringField("First Name: ", validators=[DataRequired()])
    last_name = StringField("Last Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    phone_number = IntegerField("Phone Number: ", validators=[DataRequired()])
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField('Sign Up!')

class vieworder(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField('Submit')

class update_customer(FlaskForm):
    first_name = StringField("First Name: ", validators=[DataRequired()])
    last_name = StringField("Last Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    phone_number = IntegerField("Phone Number: ", validators=[DataRequired()])
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField('Press to Update!')

class update_order(FlaskForm):
    order_id = IntegerField("Order ID: ", validators=[DataRequired()])
    customer_id = IntegerField("Customer ID: ", validators=[DataRequired()])
    date_placed = DateField("Date Placed: ", validators=[DataRequired()])
    order_status = StringField("Order Status: ", validators=[DataRequired()])
    submit = SubmitField('Press to Update Your Order!')

class delete_order(FlaskForm):
    order_id = IntegerField("Order ID: ", validators=[DataRequired()])
    customer_id = IntegerField("Customer ID: ", validators=[DataRequired()])
    submit = SubmitField('Press to Delete Your Order!')

class delete_customer(FlaskForm):
    customer_id = IntegerField("Customer ID: ", validators=[DataRequired()])
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField('Press to Update!')
