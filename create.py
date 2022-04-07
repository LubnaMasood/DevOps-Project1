from application import db
from application.models import Customer, Customer_order

db.drop_all()
db.create_all()

customer1= Customer(first_name="Henry", last_name="Lake", email="Henry123@gmail.com", phone_number="07569781246", username="Henry1x", password="LittleHouse12")
db.session.add(customer1)
db.session.commit()

customer_order1= Customer_order(order_id="786", customer_id="8761", date_placed="03-04-2022", order_status="shipped")
db.session.add(customer_order1)
db.session.commit() 