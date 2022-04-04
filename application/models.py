from app import db 

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(40), unique=True)
    phone_number = db.Column(db.Integer())

class Customer_orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer())
    product_id = db.Column(db.Integer())
    date_placed = db.Column(db.DateTime)
    order_status = db.Column(db.String(35), nullable=False)
    
class Makeup_Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Numeric)
    stock = db.Column(db.Integer())
