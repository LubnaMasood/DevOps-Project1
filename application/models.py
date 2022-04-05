from app import db 

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(40), unique=True)
    phone_number = db.Column(db.Integer())
    username = db.Column(db.String(35), unique = True)
    password = db.Column(db.String(35))
    customer_order = db.relationship('customer_order', backref='customerbr')

class Customer_order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date_placed = db.Column(db.DateTime)
    order_status = db.Column(db.String(35), nullable=False)
    customer = db.relationship('Customer', backref='customerorderrbr')
