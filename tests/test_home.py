from app import app
import unittest
import json


class MyTestCase(unittest.TestCase):


    def setUp(self) -> None:
        app.testing = True
        self.app = app.test_client()


    def test_index(self):
        response = self.app.get('/api')
        data = response.data.decode('utf-8')

        assert response.status_code == 200

    def test_books(self):
        response = self.app.get('/api/books')
        data = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert type(data) is list