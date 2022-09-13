import unittest
import requests
import json
import hashlib

URL = 'http://127.0.0.1:8000/api/v1'

class EditUserName_Module(unittest.TestCase):
    architectUsername = "testarchitect"
    architectPassword = "K5SJl8WbWz"
    cookerUsername = "testcooker"
    cookerPassword = "VTbXkp1AGd"
    chefUsername = "testchef"
    chefPassword = "0abtxnRZ8F"

    #功能方法
    def login_getToken(self,username,password):
        loginr = requests.post(URL + '/admin/user/login',
                          json={"username" : username,
                                "password" : password})
        obj = json.loads(loginr.text)
        if (obj['code']=="00000"):
            print("login successfully")
            return obj['data']['token']
        else:
            print('login failed error Code:'+obj['code'])

    #md5 加密
    def exchange_to_md5(self, content) :
        # 创建md5对象
        md_obj = hashlib.md5()
        # 传入信息进行加密，注意传入的信息必须进行encode编码，否则报错
        md_obj.update(content.encode("utf-8"))
        # 获取加密后的信息
        md_res = md_obj.hexdigest()
        return md_res

    # 修改用户名: 三种身份
    def test_changeUsername_chef(self):
        token = self.login_getToken(self.chefUsername,self.exchange_to_md5(self.chefPassword))
        r = requests.post(URL+'/admin/user/changeUsername',
                          headers={"token": token},
                          json={"username": "newchefname"})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)

    def test_changeUsername_cooker(self):
        token = self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        r = requests.post(URL+'/admin/user/changeUsername',
                          headers={"token": token},
                          json={"username": "newcookername"})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)

    def test_changeUsername_architect(self):
        token = self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r = requests.post(URL+'/admin/user/changeUsername',
                          headers={"token": token},
                          json={"username": "newarchitectname"})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)

    @classmethod
    def setUpClass(cls):
        chefToken = cls.login_getToken(cls,'newchefname',cls.exchange_to_md5(cls,cls.chefPassword))
        requests.post(URL+'/admin/user/changeUsername',
                          headers={"token": chefToken},
                          json={"username": "testchef"})
        cookerToken = cls.login_getToken(cls,'newcookername',cls.exchange_to_md5(cls,cls.cookerPassword))
        requests.post(URL+'/admin/user/changeUsername',
                          headers={"token": cookerToken},
                          json={"username": "testcooker"})
        architectToken = cls.login_getToken(cls,'newarchitectname',cls.exchange_to_md5(cls,cls.architectPassword))
        requests.post(URL+'/admin/user/changeUsername',
                          headers={"token": architectToken},
                          json={"username": "testarchitect"})


    @classmethod
    def tearDownClass(cls):
        chefToken = cls.login_getToken(cls,'newchefname',cls.exchange_to_md5(cls,cls.chefPassword))
        requests.post(URL+'/admin/user/changeUsername',
                          headers={"token": chefToken},
                          json={"username": "testchef"})
        cookerToken = cls.login_getToken(cls,'newcookername',cls.exchange_to_md5(cls,cls.cookerPassword))
        requests.post(URL+'/admin/user/changeUsername',
                          headers={"token": cookerToken},
                          json={"username": "testcooker"})
        architectToken = cls.login_getToken(cls,'newarchitectname',cls.exchange_to_md5(cls,cls.architectPassword))
        requests.post(URL+'/admin/user/changeUsername',
                          headers={"token": architectToken},
                          json={"username": "testarchitect"})

if __name__ == '__main__' :
    unittest.main()