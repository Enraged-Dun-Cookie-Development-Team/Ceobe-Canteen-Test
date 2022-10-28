from Backend.User.Login import login_test
import unittest

initialUsername = "ceobe"
initialPassword = "fdb04988b4e48c4f16952457e86b8d25"
architectUsername = "testarchitect"
architectPassword = "K5SJl8WbWz"
cookerUsername = "testcooker"
cookerPassword = "VTbXkp1AGd"
chefUsername = "testchef"
chefPassword = "0abtxnRZ8F"

s=unittest.TestSuite()
data=[('test_login',cookerUsername,cookerPassword,None),
      ('test_login',cookerUsername,'123','A0004'),
      ('test_login',chefUsername,chefPassword,None),
      ('test_login',chefUsername,'123','A0004'),
      ('test_login',architectUsername,architectPassword,None),
      ('test_login',architectUsername,'123','A0004')]

for i in data:
    s.addTest(login_test.Login_test(*i))

r=unittest.TextTestRunner()
r.run(s)