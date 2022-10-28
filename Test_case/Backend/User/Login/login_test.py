import unittest
import login


class Login_test(unittest.TestCase):
    def __init__(self , method, username, password, ex):
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
            print("该用例未通过")
            result = '不通过'
            raise e
        else:
            print("该用例通过")
            result = '通过'
