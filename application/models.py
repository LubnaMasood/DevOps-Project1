from application import db 

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(40), unique=True)
    phone_number = db.Column(db.String(), unique=True)
    username = db.Column(db.String(35), unique = True)
    password = db.Column(db.String(35))
    order = db.relationship('Customer_order', backref='customer')

class Customer_order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date_placed = db.Column(db.DateTime)
    order_status = db.Column(db.String(35), nullable=False)
 
    