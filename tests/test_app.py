from application import app, db
from application.models import Customer, Customer_order
from flask import url_for, request, redirect, render_template
from flask_testing import TestCase
from datetime import datetime

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///data.db', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app
    
    def setUp(self):
        db.create_all()
        test_customer1 = Customer(first_name='test_first_name', last_name='test_last_name', email='test_email', phone_number='test_phone_number', username='test_username', password='test_password', id=1)
        db.session.add(test_customer1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestCreate(TestBase):
    def test_create(self):
        response = self.client.post(url_for('create'), data=dict(first_name="test_first_name", last_name="test_last_name", email="test_email", phone_number="test_phone_number", username="test_username", password="test_password"), follow_redirects=True)
        assert 'Enter A Customer'in response.data.decode()

class TestDelete(TestBase):
    def test_delete_customer(self):
        response = self.client.get(url_for('deletecustomer', id=1, follow_redirects=True))
        assert 'Homepage' in response.data.decode()

class TestViews(TestBase):
    def test_homepage(self):
        response = self.client.get(url_for('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_create_customer(self):
        response = self.client.get(url_for('create_customer'))
        self.assertEqual(response.status_code, 302)
    
    def test_create(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_addorder(self):
        response = self.client.get(url_for('addorder'))
        self.assertEqual(response.status_code, 200)
    
    def test_updateorder(self):
        response = self.client.get(url_for('updateorder', id=1))
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.get(url_for('delete', id=1))
        self.assertEqual(response.status_code, 302)
    
    def test_deletecustomer(self):
        response = self.client.get(url_for('deletecustomer', id=1))
        self.assertEqual(response.status_code, 302)
