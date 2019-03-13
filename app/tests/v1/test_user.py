import unittest
from app import app
import json

class TestUser(unittest.TestCase):
    '''Tests fetching of all users delivery orders'''
    def test_get_users(self):
        self.response = app.test_client().get('/api/v1/users/')
        self.assertEqual(self.response.status_code, 200)

    '''Tests fetching of all delivery orders made by specific user'''
    def test_get_all_orders_by_specific_user(self):
        self.response = app.test_client().get('/api/v1/users/0/parcels')
        self.assertEqual(self.response.status_code, 200)

    '''Test creation of a parcel deliver order'''
    def test_post_user(self):
        self.response = app.test_client().post(
            'api/v1/users/',
            data=json.dumps(
                dict(
                    firstname = "wafula",
                    lastname = "wafush",
                    othernames = "ww",
                    email = "mail",
                    username = "namename",
                    registered = "date registered",
                    isAdmin = False
                )
            ), content_type='application/json'
        )
        self.assertEqual(self.response.status_code, 201)