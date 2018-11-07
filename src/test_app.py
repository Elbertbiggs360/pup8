''' test file for main module '''

import unittest
import json

from app import create_app

class BaseTest(unittest.TestCase):
  def setUp(self):
    self.app = create_app('testing')
    self.client = self.app.test_client

  def test_get_request_works(self):
    res = self.client().get('/')
    self.assertEqual(res.status_code, 200)

  def test_get_request_returns_right_payload(self):
    res = self.client().get('/')
    res_data = json.loads(res.data)
    self.assertEqual(res_data, {'Fellow': 'Bruce'})

  def test_post_request_201(self):
    res = self.client().post('/')
    self.assertEqual(res.status_code, 201)

if __name__ == '__main__':
  unittest.main()