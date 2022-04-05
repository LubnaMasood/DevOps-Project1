from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, EmailField
from wtforms.validators import data_required


class SignUpForm(FlaskForm):
    first_name = StringField("First Name: ", validators=[data_required()])
    last_name = StringField("Last Name: ", validators=[data_required()])
    email = StringField("Email: ", validators=[data_required()])
    phone_number = IntegerField("Phone Number: ", validators=[data_required()])
    username = StringField("Username: ", validators=[data_required()])
    password = PasswordField("Password: ", validators=[data_required()])
    submit = SubmitField('Submit')

class ViewOrderForm(FlaskForm):
    username = StringField("Username: ", validators=[data_required()])
    password = PasswordField("Password: ", validators=[data_required()])
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    old_email = EmailField("Old Email: ", validators=[data_required()])
    new_email = EmailField("New Email: ", validators=[data_required()])
    submit = SubmitField('Update')
    