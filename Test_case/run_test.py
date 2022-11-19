from Backend.User.Login import login_test
from Test_case.Common.config_parse import config_parse
import unittest


userdata=config_parse()["Accounts"]

s=unittest.TestSuite()
data=[('test_login',userdata["chef"]["username"],userdata["chef"]["password"],"00000"),
      ('test_login',userdata["chef"]["username"],'123','A0004'),
      ('test_login',userdata["cooker"]["username"],userdata["cooker"]["password"],"00000"),
      ('test_login',userdata["cooker"]["username"],'123','A0004'),
      ('test_login',userdata["architect"]["username"],userdata["architect"]["password"],"00000"),
      ('test_login',userdata["architect"]["username"],'123','A0004'),
      ('test_getInfo',userdata["chef"]["username"],userdata["chef"]["password"],"00000"),
      ('test_getInfo',userdata["architect"]["username"],userdata["architect"]["password"],"00000"),
      ('test_getInfo',userdata["cooker"]["username"],userdata["cooker"]["password"],"00000")]

for i in data:
    s.addTest(login_test.Login_test(*i))

r=unittest.TextTestRunner()
r.run(s)