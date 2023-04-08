import json
import unittest
from app import app
from flask_testing import TestCase

class TestAuthApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_register(self):
        valid_data = {
            'username': 'test_user',
            'password': 'test_password'
        }

        response = self.client.post('/register', data=json.dumps(valid_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'success': 'User test_user registered successfully.'})

        invalid_data = {
            'username': 'test_user',
            'password': 123456
        }

        response = self.client.post('/register', data=json.dumps(invalid_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        register_data = {
            'username': 'test_user',
            'password': 'test_password'
        }

        self.client.post('/register', data=json.dumps(register_data), content_type='application/json')

        valid_data = {
            'username': 'test_user',
            'password': 'test_password'
        }

        response = self.client.post('/login', data=json.dumps(valid_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'success': 'Access granted for user test_user.'})

        invalid_data = {
            'username': 'test_user',
            'password': 'wrong_password'
        }

        response = self.client.post('/login', data=json.dumps(invalid_data), content_type='application/json')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
