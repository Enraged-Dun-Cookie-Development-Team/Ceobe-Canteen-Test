import unittest
import requests
import json
import hashlib

URL = 'http://127.0.0.1:8000'

#
# 针对用户模块的测试类
class User_Module(unittest.TestCase) :
    # 需要储存为后续测试所用变量
    initialUsername="ceobe"
    # md5加密后的
    initialPassword="fdb04988b4e48c4f16952457e86b8d25"
    initialToken="7GHd823hf8D33"
    architectUsername="LosJoxU74Z"
    architectPassword="6ISuwgpMEE"
    # chefUsername=>editedname
    chefUsername="sWlRWPSF50"
    chefPassword="YPMcFGCkBT"

    def test_login(self) :
        r = requests.post(URL + '/api/v1/admin/user/login',
                          json={"username": self.chefUsername,
                                "password": self.exchange_to_md5(self.chefPassword)})
        obj = json.loads(r.text)
        assert obj['code'] is None

    # 错误登录(账号密码错误)是否会给token
    def test_errorlogin(self):
        r = requests.post(URL + '/api/v1/admin/user/login',
                          json={'username' : "ceobe",
                                'password' : "1234567"})

        obj = json.loads(r.text)
        assert obj['data'] is None

    # 新建用户测试：Architect
    def test_createUser_common_architect(self) :
        r = requests.post(URL + '/api/v1/admin/user/create?permission=architect',
                          headers={"token": self.login_getToken(self.initialUsername,self.initialPassword)})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)  # 判断是否不返回错误结果码
        if(obj['code']==None):
            self.newerArchitectUsername=obj['data']['username']
            self.newerArchitectPassword=obj['data']['password']
            print(r.text)

    # 新建用户测试：Cooker
    def test_createUser_common_cooker(self) :
        r = requests.post(URL + '/api/v1/admin/user/create?permission=cooker',
                          headers={"token": self.login_getToken(self.initialUsername,self.initialPassword)})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)
        if(obj['code']==None):
            self.newerCookerUsername=obj['data']['username']
            self.newerCookerPassword=obj['data']['password']

    # 新建用户测试：Chef
    def test_createUser_common_chef(self) :
        r = requests.post(URL + '/api/v1/admin/user/create?permission=chef',
                          headers={"token": self.login_getToken(self.initialUsername,self.initialPassword)})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)
        if(obj['code']==None):
            self.newerChefUsername=obj['data']['username']
            self.newerChefPassword=obj['data']['password']
            print(r.text)

    # 错误Token新建用户测试： Architect
    def test_createUser_withWrongToken_architect(self):
        r = requests.post(URL + '/api/v1/admin/user/create?permission=architect',
                          headers={"token": "123"})
        obj = json.loads(r.text)
        self.assertEqual(obj['data'], None)

    # 错误Token新建用户测试： Cooker
    def test_createUser_withWrongToken_architect(self):
        r = requests.post(URL + '/api/v1/admin/user/create?permission=cooker',
                          headers={"token": "123"})
        obj = json.loads(r.text)
        self.assertEqual(obj['data'], None)

    # 错误Token新建用户测试： Chef
    def test_createUser_withWrongToken_architect(self):
        r = requests.post(URL + '/api/v1/admin/user/create?permission=architect',
                          headers={"token": "123"})
        obj = json.loads(r.text)
        self.assertEqual(obj['data'], None)

    #md5 加密
    def exchange_to_md5(self, content) :
        # 创建md5对象
        md_obj = hashlib.md5()
        # 传入信息进行加密，注意传入的信息必须进行encode编码，否则报错
        md_obj.update(content.encode("utf-8"))
        # 获取加密后的信息
        md_res = md_obj.hexdigest()
        return md_res

    # 获取用户信息
    def test_getUserInfo(self):
        # 登录初始账号
        token=self.login_getToken(self.initialUsername,self.initialPassword)
        r = requests.get(URL + '/admin/user/info',
                          headers={'token': token})
        obj = json.loads(r.text)
        if(obj['code'] is not None):
            print(obj)
        self.assertEqual(obj['data']['roles'][0], "chef")
        self.assertEqual(obj['data']['name'], "ceobe")

    def login_getToken(self,username,password):
        loginr = requests.post(URL + '/api/v1/admin/user/login',
                          json={"username" : username,
                                "password" : password})
        obj = json.loads(loginr.text)
        if (obj['code']==None):
            print("login successfully")
            return obj['data']['token']
        else:
            print('login failed error Code:'+obj['code'])

    # 修改用户名
    def test_changeUsername(self):
        # 登录账号
        token = self.login_getToken(self.chefUsername,self.exchange_to_md5(self.chefPassword))
        r = requests.post(URL + '/api/v1/admin/user/changeUsername',
                          headers={"token": token},
                          json={"username": "editedname"})
        obj = json.loads(r.text)
        if(obj['code'] is not None):
            print(obj)
        self.assertEqual(obj['data']['username'], "editedname")
        self.chefUsername="editedname"

    # 修改密码
    def test_changePassword(self):
        tokenc=self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r = requests.post(URL + '/api/v1/admin/user/changeUsername',
                          headers={"token": tokenc},
                          json={"old_password" : self.exchange_to_md5(self.architectPassword),
                                  "new_password" : self.exchange_to_md5("changedpassword")})
        obj = json.loads(r.text)
        if(obj['code'] is not None):
            print(obj)
        self.assertEqual(obj['code'],None)
        self.architectPassword="changedpassword"

if __name__ == '__main__' :
    unittest.main()
