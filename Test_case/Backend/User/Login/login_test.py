import unittest
from . import login


class Login_test(unittest.TestCase):
    def __init__(self , method, username, password,ex):
        super().__init__(method)
        self.username=username
        self.password=password
        self.ex=ex

    def test_login(self):
        result= login.login_check(self.username, self.password)
        excepted = result['code']

        try:
            self.assertEqual(excepted, self.ex)
        except AssertionError as e:
            print("FAILED")
            result = 'failed'
            raise e
        else:
            print("PASS")
            result = 'pass'

    def test_getInfo(self):
        result= login.getInfo_check(self.username, self.password)
        excepted = result['code']

        try:
            self.assertEqual(excepted, self.ex)
        except AssertionError as e:
            print("FAILED")
            result = 'failed'
            raise e
        else:
            print("PASS")
            result = 'pass'

