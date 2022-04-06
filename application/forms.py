from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, EmailField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError


class SignUpForm(FlaskForm):
    first_name = StringField("First Name: ", validators=[DataRequired()])
    last_name = StringField("Last Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    phone_number = IntegerField("Phone Number: ", validators=[DataRequired()])
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField('Sign Up!')

class ViewOrderForm(FlaskForm):
    username = StringField("Username: ", validators=[data_required()])
    password = PasswordField("Password: ", validators=[data_required()])
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    old_email = EmailField("Old Email: ", validators=[data_required()])
    new_email = EmailField("New Email: ", validators=[data_required()])
    submit = SubmitField('Update')
    