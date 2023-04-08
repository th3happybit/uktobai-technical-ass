import json
import unittest
from app import app
from flask_testing import TestCase

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_sum_numbers(self):
        valid_data = {
            'numbers': [1, 2, 3, 4, 5]
        }

        response = self.client.post('/sum', data=json.dumps(valid_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'sum': 15})

        invalid_data = {
            'numbers': [1, 'two', 3, 4, 5]
        }

        response = self.client.post('/sum', data=json.dumps(invalid_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_concatenate_strings(self):
        valid_data = {
            'string1': 'Hello, ',
            'string2': 'World!'
        }

        response = self.client.post('/concatenate', data=json.dumps(valid_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'concatenated': 'Hello, World!'})

        invalid_data = {
            'string1': 'Hello, ',
            'string2': 123
        }

        response = self.client.post('/concatenate', data=json.dumps(invalid_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
