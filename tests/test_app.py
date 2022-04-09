from app import app, db
from application.models import Customer, Customer_order
from application.forms import CustomerForm, Customer_orderForm
from flask import request, redirect, url_for, render_template
from falsk_testing import TestCase

class TestApp(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///data.db', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app
        

    def setUp(self):
        db.create_all()
        test_customer1 = Customer(
        test_order1

        db.session.add(test_customer)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestApp):

    def test_homepage_get(self):
        response = self.client.get(url_for('homepage'))
        self.assertEqual(response.status_code, 200)
    
    def test_create_customer_get(self):
        response = self.client.get(url_for('create_customer'))
        self.assertEqual(response.status_code, 200)

    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_addorder_get(self):
        response = self.client.get(url_for('addorder'))
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code, 200)
    
    def test_updateorder_get(self):
        response = self.client.get(url_for('updateorder'))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code, 200)

    def test_deletecustomer_get(self):
        response = self.client.get(url_for('deleteorder'))
        self.assertEqual(response.status_code, 200)



    def test_post_req(self):
        response = self.client.post(url_for('CustomerForm'), data = dict(first_name="Henry", last_name="Lake"), follow_redirects=True)
        self.assertIn(b'', response.data)
