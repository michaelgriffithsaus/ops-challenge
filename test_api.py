import unittest
import json
import os
import sys

# Pathing change so that the tests can correctly discover the app modules
testdir = os.path.dirname(__file__)
srcdir = '../app/'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from app import app

class TestAPIRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    
    #Sunny Day scenario Tests for the hello world class
    # Route = /
    def test_that_hello_world_returns_200(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_that_hello_world_returns_correct_content(self):
        correctResponse = {'hello': 'world'}
        response = self.app.get('/')
        responseContent = json.loads(response.get_data())
        self.assertEqual(responseContent, correctResponse)

    #Sunny Day scenario Test for the health class
    # Route = /health

    def test_that_health_returns_200_when_healthy(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_that_health_returns_UP_when_healthy(self):
        correctResponse = {'Status' : 'UP'}
        
        response = self.app.get('/health')
        responseContent = json.loads(response.get_data())

        self.assertEqual(responseContent, correctResponse)
    
    #Sunny Day scenario Test for the metadata class
    # Route = /metadata

    def test_that_metadata_returns_200(self):
        response = self.app.get('/metadata')
        self.assertEqual(response.status_code, 200)

    
    def test_that_metadata_returns_metadata(self):
        correctResponse = {
            "myapplication": [
                {
                    "version": "1.0",
                    "description" : "pre-interview technical test",
                    "lastcommitsha": "abc57858585"
                }
            ]
            }
        
        response = self.app.get('/metadata')
        responseContent = json.loads(response.get_data())

        self.assertEqual(responseContent, correctResponse)

        

if __name__ == '__main__':
    unittest.main()