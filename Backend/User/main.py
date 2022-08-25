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
    # 如果修改用户名和密码测试通过 账号密码=edited+身份    e.g.editedchef
    # architect username : "LosJoxU74Z" password: "changedpassword"
    architectUsername=""
    architectPassword=""
    # cooker "username":"oquG3k9f1D","password":"f30inzJ5yD"
    cookerUsername=""
    cookerPassword=""
    # chef username "editedname" password "YPMcFGCkBT"
    chefUsername=""
    chefPassword=""

    #功能方法
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

    #md5 加密
    def exchange_to_md5(self, content) :
        # 创建md5对象
        md_obj = hashlib.md5()
        # 传入信息进行加密，注意传入的信息必须进行encode编码，否则报错
        md_obj.update(content.encode("utf-8"))
        # 获取加密后的信息
        md_res = md_obj.hexdigest()
        return md_res

    # 新建三种用户测试正常情况和用错误token情况
    # 新建用户测试：Architect
    def test_createUser_common_architect(self) :
        r = requests.post(URL + '/api/v1/admin/user/create?permission=architect',
                          headers={"token": self.login_getToken(self.initialUsername,self.initialPassword)})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)  # 不返回结果码为正常响应情况
        if(obj['code']==None):
            self.architectUsername=obj['data']['username']  # 收集账号密码为后续登录接口
            self.architectPassword=obj['data']['password']

    # 新建用户测试：Cooker
    def test_createUser_common_cooker(self) :
        r = requests.post(URL + '/api/v1/admin/user/create?permission=cooker',
                          headers={"token": self.login_getToken(self.initialUsername,self.initialPassword)})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)
        if(obj['code']==None):
            self.cookerUsername=obj['data']['username']
            self.cookerPassword=obj['data']['password']

    # 新建用户测试：Chef
    def test_createUser_common_chef(self) :
        r = requests.post(URL + '/api/v1/admin/user/create?permission=chef',
                          headers={"token": self.login_getToken(self.initialUsername,self.initialPassword)})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)
        if(obj['code']==None):
            self.chefUsername=obj['data']['username']
            self.chefPassword=obj['data']['password']

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
        r = requests.post(URL + '/api/v1/admin/user/create?permission=chef',
                          headers={"token": "123"})
        obj = json.loads(r.text)
        self.assertEqual(obj['data'], None)

    # 登录接口测试
    # 三种权限及错误情况
    def test_login_chef(self) :
        r = requests.post(URL + '/api/v1/admin/user/login',
                          json={"username": self.chefUsername,
                                "password": self.exchange_to_md5(self.chefPassword)})
        obj = json.loads(r.text)
        assert obj['code'] is None

    # 错误登录(账号密码错误)是否会给token
    def test_errorlogin_chef(self):
        r = requests.post(URL + '/api/v1/admin/user/login',
                          json={'username' : "ceobe",
                                'password' : "1234567"})
        obj = json.loads(r.text)
        assert obj['data'] is None

    def test_login_cooker(self) :
        r = requests.post(URL + '/api/v1/admin/user/login',
                          json={"username": self.cookerUsername,
                                "password": self.exchange_to_md5(self.cookerPassword)})
        obj = json.loads(r.text)
        assert obj['code'] is None

    def test_errorlogin_cooker(self):
        r = requests.post(URL + '/api/v1/admin/user/login',
                          json={'username' : self.cookerUsername,
                                'password' : "1234567"})
        obj = json.loads(r.text)
        assert obj['data'] is None

    def test_login_architect(self) :
        r = requests.post(URL + '/api/v1/admin/user/login',
                          json={"username": self.architectUsername,
                                "password": self.exchange_to_md5(self.architectPassword)})
        obj = json.loads(r.text)
        assert obj['code'] is None

    # 错误登录(账号密码错误)是否会给token
    def test_errorlogin_architect(self):
        r = requests.post(URL + '/api/v1/admin/user/login',
                          json={'username' : self.architectUsername,
                                'password' : "1234567"})
        obj = json.loads(r.text)
        assert obj['data'] is None


    # 获取用户信息:三种权限情况
    def test_getUserInfo_chef(self):
        token=self.login_getToken(self.chefUsername,self.chefPassword)
        r = requests.get(URL + '/admin/user/info',
                          headers={'token': token})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'],None)
        self.assertEqual(obj['data']['roles'][0], "chef")
        self.assertEqual(obj['data']['name'], self.chefUsername)

    def test_getUserInfo_cooker(self):
        token=self.login_getToken(self.cookerUsername,self.cookerPassword)
        r = requests.get(URL + '/admin/user/info',
                          headers={'token': token})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'],None)
        self.assertEqual(obj['data']['roles'][0], "cooker")
        self.assertEqual(obj['data']['name'], self.cookerUsername)

    def test_getUserInfo_architect(self):
        token=self.login_getToken(self.architectUsername,self.architectPassword)
        r = requests.get(URL + '/admin/user/info',
                          headers={'token': token})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'],None)
        self.assertEqual(obj['data']['roles'][0], "architect")
        self.assertEqual(obj['data']['name'], self.architectUsername)


    # 修改用户名: 三种身份
    def test_changeUsername_chef(self):
        token = self.login_getToken(self.chefUsername,self.exchange_to_md5(self.chefPassword))
        r = requests.post(URL + '/api/v1/admin/user/changeUsername',
                          headers={"token": token},
                          json={"username": "editedchef"})
        obj = json.loads(r.text)
        if(obj['code'] is not None):
            print(obj)
        self.assertEqual(obj['data']['username'], "editedchef")
        self.chefUsername="editedchef"

    def test_changeUsername_cooker(self):
        token = self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        r = requests.post(URL + '/api/v1/admin/user/changeUsername',
                          headers={"token": token},
                          json={"username": "editedcooker"})
        obj = json.loads(r.text)
        if(obj['code'] is not None):
            print(obj)
        self.assertEqual(obj['data']['username'], "editedcooker")
        self.cookerUsername="editedcooker"

    def test_changeUsername_architect(self):
        token = self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r = requests.post(URL + '/api/v1/admin/user/changeUsername',
                          headers={"token": token},
                          json={"username": "editedarchitect"})
        obj = json.loads(r.text)
        if(obj['code'] is not None):
            print(obj)
        self.assertEqual(obj['data']['username'], "editedarchitect")
        self.architectUsername="editedarchitect"

    # 修改密码:三种身份
    def test_changePassword_chef(self):
        tokenc=self.login_getToken(self.chefUsername,self.exchange_to_md5(self.chefPassword))
        r = requests.post(URL + '/api/v1/admin/user/changeUsername',
                          headers={"token": tokenc},
                          json={"old_password" : self.exchange_to_md5(self.chefPassword),
                                  "new_password" : self.exchange_to_md5("editedchef")})
        obj = json.loads(r.text)
        if(obj['code'] is not None):
            print(obj)
        self.assertEqual(obj['code'],None)
        self.architectPassword="editedchef"

    def test_changePassword_cooker(self):
        tokenc=self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        r = requests.post(URL + '/api/v1/admin/user/changeUsername',
                          headers={"token": tokenc},
                          json={"old_password" : self.exchange_to_md5(self.cookerPassword),
                                  "new_password" : self.exchange_to_md5("editedcooker")})
        obj = json.loads(r.text)
        if(obj['code'] is not None):
            print(obj)
        self.assertEqual(obj['code'],None)
        self.cookerPassword="editedcooker"

    def test_changePassword_architect(self):
        tokenc=self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r = requests.post(URL + '/api/v1/admin/user/changeUsername',
                          headers={"token": tokenc},
                          json={"old_password" : self.exchange_to_md5(self.architectPassword),
                                  "new_password" : self.exchange_to_md5("editedarchitect")})
        obj = json.loads(r.text)
        if(obj['code'] is not None):
            print(obj)
        self.assertEqual(obj['code'],None)
        self.architectPassword="editedarchitect"

if __name__ == '__main__' :
    unittest.main()
