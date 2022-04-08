from application import db
from application.models import Customer, Customer_order

db.create_all()

customer1= Customer(first_name="Jake", last_name="Cain", email="Jake796@gmail.com", phone_number="75600824", username="Jake786", password="Dubai_87")
db.session.add(customer1)
db.session.commit()

customer_order1= Customer_order(id="786", order_id="8761", date_placed="2022-066-03", order_status="shipped")
db.session.add(customer_order1)
db.session.commit() 