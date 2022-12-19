import request_test
from Common.config_parse import config_parse
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
      ('test_getInfo',userdata["cooker"]["username"],userdata["cooker"]["password"],"00000"),
      ('test_getUserList', userdata["chef"]["username"], userdata["chef"]["password"], "00000"),
      ('test_getUserList', userdata["architect"]["username"], userdata["architect"]["password"], "A0002"),
      ('test_getUserList', userdata["cooker"]["username"], userdata["cooker"]["password"], "00000"),
      ('test_getAnnouncement', userdata["chef"]["username"], userdata["chef"]["password"], "00000"),
      ('test_getAnnouncement', userdata["architect"]["username"], userdata["architect"]["password"], "A0002"),
      ('test_getAnnouncement', userdata["cooker"]["username"], userdata["cooker"]["password"], "00000"),
      ('test_getCurrentVideoInfo', userdata["chef"]["username"], userdata["chef"]["password"], "00000"),
      ('test_getCurrentVideoInfo', userdata["architect"]["username"], userdata["architect"]["password"], "A0002"),
      ('test_getCurrentVideoInfo', userdata["cooker"]["username"], userdata["cooker"]["password"], "00000"),
      ('test_getResource', userdata["chef"]["username"], userdata["chef"]["password"], "00000"),
      ('test_getResource', userdata["architect"]["username"], userdata["architect"]["password"], "A0002"),
      ('test_getResource', userdata["cooker"]["username"], userdata["cooker"]["password"], "00000"),
      ('test_getRecentMansionId', userdata["chef"]["username"], userdata["chef"]["password"], "00000"),
      ('test_getRecentMansionId', userdata["architect"]["username"], userdata["architect"]["password"], "00000"),
      ('test_getRecentMansionId', userdata["cooker"]["username"], userdata["cooker"]["password"], "A0002")
      ]

for i in data:
    s.addTest(request_test.Basic_test(*i))

r=unittest.TextTestRunner()
r.run(s)