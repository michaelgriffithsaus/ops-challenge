import unittest
import json
from app import APP

class TestAPIRoutes(unittest.TestCase):

    """
        Contains all Test Cases for testing the app's API endpoints.
        When invoked the SetUp will run first and initialise the app.
        The app will stay initialised through the test session.
        Given the low complexity of the app no tear down method has been implemented.
    """

    def setUp(self):
        self.app = APP.test_client()

    #Sunny Day scenario Tests for the hello world class
    # Route = /
    def test_that_hello_world_returns_200(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_that_hello_world_returns_correct_content(self):
        correct_response = {'hello': 'world'}
        response = self.app.get('/')
        response_content = json.loads(response.get_data())
        self.assertEqual(response_content, correct_response)

    #Sunny Day scenario Test for the health class
    # Route = /health

    def test_that_health_returns_200_when_healthy(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_that_health_returns_UP_when_healthy(self):
        correct_response = {'status' : 'UP'}

        response = self.app.get('/health')
        response_content = json.loads(response.get_data())

        self.assertEqual(response_content, correct_response)
    
    #Sunny Day scenario Test for the metadata class
    # Route = /metadata

    def test_that_metadata_returns_200(self):
        response = self.app.get('/metadata')
        self.assertEqual(response.status_code, 200)

    
    def test_that_metadata_returns_metadata(self):
        correct_response = {
            "app_description": "Pre-interview technical test"
            }
        
        response = self.app.get('/metadata')
        response_content = json.loads(response.get_data())

        self.assertEqual(response_content, correct_response)


if __name__ == '__main__':
    unittest.main()
