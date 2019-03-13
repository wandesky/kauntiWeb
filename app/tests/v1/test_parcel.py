import unittest
from app import app
import json

class TestParcel(unittest.TestCase):
    '''Tests fetching of all parcel delivery orders'''
    def test_get_parcels(self):
        self.response = app.test_client().get('/api/v1/parcels/')
        self.assertEqual(self.response.status_code, 200)

    '''Tests fetching of a specific parcel delivery order'''
    def test_get_parcel(self):
        self.response = app.test_client().get('/api/v1/parcels/0')
        self.assertEqual(self.response.status_code, 200)

    '''Test creation of a parcel deliver order'''
    def test_post_parcel(self):
        self.response = app.test_client().post(
            'api/v1/parcels/',
            data=json.dumps(
                dict(
                    placedBy = "wafula",
                    weight = "2kg",
                    weightmetric = "dummyweightmetric",
                    sentOn = "dummysentOn",
                    deliveredOn = "dummydeliveredOn",
                    status = "dummystatus",
                    parcel_from = "dummyparcel_from",
                    parcel_to = "dummyparcel_to",
                    currentlocation = "dummycurrentlocation"
                )
            ), content_type='application/json'
        )
        self.assertEqual(self.response.status_code, 201)