from src.app import create_app
import unittest
import json

class TestApp(unittest.TestCase):
  def setUp(self):
    self.app = create_app()
    self.client = self.app.test_client
    self.payload = {'Home': 'Welcome Home'}
  
  def test_get_request_successfull(self):
    res = self.client().get('/')
    self.assertEqual(res.status_code, 200)

  def test_request_returns_payload(self):
    res = self.client().get('/')
    self.assertEqual(self.payload, json.loads(res.data))

  def tearDown(self):
    pass


if __name__ == '__main__':
  unittest.main()
