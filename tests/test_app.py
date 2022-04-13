from application import app, db
from application.models import Customer, Customer_order
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///data.db', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app
        

    def setUp(self):
        db.create_all()
#         test_customer = Customer(first_name="test_first_name", last_name="test_last_name", email="test_email", phone_number="test_phone_number", username="test_username", password="test_password", id=1)
#         test_customer_order = Customer_order(id="test_id", date_placed="test_date_placed", order_status="test_order_status")
#         db.session.add(test_customer)
#         db.session.add(test_customer_order)
#         db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

# class TestRead(TestBase):

#     def test_home(self):
#         response = self.client.post(url_for('homepage'))
#         assert 'test_first_name' in response.data.decode()
#         assert 'test_last_name' in response.data.decode()
#         assert 'test_email' in response.data.decode()
#         assert 'test_phone_number' in response.data.decode()
#         assert 'test_username' in response.data.decode()
#         assert 'test_response' in response.data.decode()

  
# class TestCreate(TestBase):

#     def test_create_customer(self):
#         response = self.client.post(url_for('create_customer'), data={"first_name": "test_first_name", "last_name": "test_last_name", "email": "test_email", "phone_number": "test_phone_number", "username": "test_username", "password": "test_password"}, follow_redirects=True)
#         assert "test_first_name, test_last_name, test_email, test_phone_number, test_username, test_password" in response.data.decode()


# class TestUpdate(TestBase):
#     def test_update(self):
#         response = self.client.post(url_for('update', id=1), data = dict(first_name="test_first_name", last_name="test_last_name", email="test_email", phone_number="test_phone_number", username="test_username", password="test_password"), follow_redirects=True)
#         assert 'test_first_name' in response.data.decode()
#         assert 'test_last_name'in response.data.decode()
#         assert 'test_email'in response.data.decode()
#         assert 'test_phone_number'in response.data.decode()
#         assert 'test_username'in response.data.decode()
#         assert 'test_password'in response.data.decode()

# class TestDelete(TestBase):

#     def test_deletecustomer(self):
#         response = self.client.get(url_for('deletecustomer', id=1), follow_redirects=True)
#         assert 'Homepage' in response.data.decode()


class TestViews(TestBase):

    def test_homepage(self):
        response = self.client.get(url_for('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_create_customer(self):
        response = self.client.get(url_for('create_customer')) 
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_addorder(self):
        response = self.client.get(url_for('addorder'))
        self.assertEqual(response.status_code, 200)
    
    def test_updateorder(self):
        response = self.client.get(url_for('updateorder', id=1))
        self.assertEqual(response.status_code, 200)

    def test_deletecustomer(self):
        response = self.client.get(url_for('deletecustomer', id=1))
        self.assertEqual(response.status_code, 200)
