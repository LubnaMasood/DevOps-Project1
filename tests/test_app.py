from app import app-innit, db, Customer, CustomerForm
from flask import request, redirect, url_for, render_template
from falsk_testing import TestCase

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///data.db', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app-innit
        

    def setUp(self):
        db.create_all()

        test_customer = Customer("Henry", "Lake", )

        db.session.add(test_customer)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('homepage'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_create_customer(self):
        response = self.client.get(url_for('create_customer'))
        self.assertEqual(response.status_code, 200)
        
        
    def test_post_req(self):
        response = self.client.post(url_for('CustomerForm'), data = dict(first_name="Henry", last_name="Lake"), follow_redirects=True)
        self.assertIn(b'', response.data)
