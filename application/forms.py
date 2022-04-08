from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, PasswordField
from wtforms.validators import ValidationError, Length, NumberRange, DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from application.models import Customer, Customer_order

class CustomerForm(FlaskForm):
    first_name = StringField("First Name: ", validators=[DataRequired(), Length(max=35)])
    last_name = StringField("Last Name: ", validators=[DataRequired(), Length(max=35)])
    email = StringField("Email: ", validators=[DataRequired(), Length(max=40)])
    phone_number = StringField("PhoneNumber: ", validators=[DataRequired(), Length(max=35)])
    username = StringField("Username: ", validators=[DataRequired(), Length(max=35)])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(max=35)])
    submit = SubmitField('Sign Up!')

class Customer_orderForm(FlaskForm):
    id = IntegerField("Order ID: ", validators=[DataRequired(), NumberRange(min=1, max=5)])
    date_placed = DateField("Date Placed: ", validators=[DataRequired()])
    order_status = StringField("Order Status: ", validators=[DataRequired(), Length(max=35)])
    submit = SubmitField('Track Order!')
