import unittest
from app import app
import json

class TestEdges(unittest.TestCase):
    '''Tests accessing the base url'''
    def test_get_base_url(self):
        self.response = app.test_client().get('/')
        self.assertEqual(self.response.status_code, 200)

    '''Tests accessing the api url'''
    def test_get_api_url(self):
        self.response = app.test_client().get('/api/')
        self.assertEqual(self.response.status_code, 200)

    '''Tests accessing the api/v1 url'''
    def test_get_api_v1_url(self):
        self.response = app.test_client().get('/api/v1/')
        self.assertEqual(self.response.status_code, 200)