import unittest
from unittest.mock import patch, Mock
from app import create_app
from app.constants import HttpStatus
 
class FlaskAppTests(unittest.TestCase):
 
    def setUp(self):
        self.app = create_app({'TESTING': True})
        self.client = self.app.test_client() 
 
    @patch('requests.get')
    def test_data_route_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = HttpStatus.OK
        mock_response.json.return_value = [
            {"id": 1, "title": "mocked title", "body": "mocked body"}
        ]
        mock_get.return_value = mock_response
 
        response = self.client.get('/data?title=mocked title')
 
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"mocked title", response.data)
 
    @patch('requests.get')
    def test_data_route_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = HttpStatus.NOT_FOUND
        mock_get.return_value = mock_response
 
        response = self.client.get('/data?title=nonexistent')
 
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Failed to fetch data", response.data)

 
if __name__ == '__main__':
    unittest.main()