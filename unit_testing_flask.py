import unittest
from unittest.mock import patch
from testing import TestingJWT


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.jwt_1 = TestingJWT('Benharushtomer@gmail.com', 'aaaaa')
        self.jwt_2 = TestingJWT('Benharushtomer@gmail.com', 'vcvcx')

    def tearDown(self):
        print('tearDown\n')

    def test_get_token(self):
        self.assertEqual(self.jwt_1.get_token(), 200)
        self.assertEqual(self.jwt_1.get_token(), 200)

    def test_get_posts(self):
        self.assertEqual(self.jwt_1.get_token(), 200)
        self.jwt_2.password = 'aaaaa'
        self.assertEqual(self.jwt_2.get_token(), 200)
        self.assertEqual(self.jwt_1.get_posts(), 200)
        self.assertEqual(self.jwt_2.get_posts(), 200)


if __name__ == '__main__':
    unittest.main()