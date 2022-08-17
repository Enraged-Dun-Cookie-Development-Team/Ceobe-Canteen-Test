import unittest
import requests
import json

URL = 'http://127.0.0.1:8000'


# 针对用户模块的测试类
class User_Module(unittest.TestCase) :
    # 需要储存为后续测试所用变量
    token=""
    newerArchitectUsername=""
    newerArchitectPassword=""
    newerCookerUsername=""
    newerCookerPassword=""
    newerChefUsername=""
    newerChefPassword=""

    # 初始用户登录设定为SetUpClass前置函数
    # 通过即登录测试通过
    @classmethod
    def SetUpClass(self) :
        r = requests.post(URL + '/api/v1/admin/user/login',
                          json={"username": "ceobe",
                                "password": "fdb04988b4e48c4f16952457e86b8d25"})
        obj = json.loads(r.text)
        self.token=obj['data']['token']

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
                          headers={"token": self.token})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)  # 判断是否不返回错误结果码
        if(obj['code']==None):
            self.newerArchitectUsername=obj['data']['username']
            self.newerArchitectPassword=obj['data']['password']

    # 新建用户测试：Cooker
    def test_createUser_common_cooker(self) :
        r = requests.post(URL + '/api/v1/admin/user/create?permission=cooker',
                          headers={"token": self.token})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)
        if(obj['code']==None):
            self.newerCookerUsername=obj['data']['username']
            self.newerCookerPassword=obj['data']['password']

    # 新建用户测试：Chef
    def test_createUser_common_chef(self) :
        r = requests.post(URL + '/api/v1/admin/user/create?permission=chef',
                          headers={"token": self.token})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)
        if(obj['code']==None):
            self.newerChefUsername=obj['data']['username']
            self.newerChefPassword=obj['data']['password']

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
        r = requests.post(URL + 'api/v1/admin/user/info',
                          headers={"token": self.token})
        obj = json.loads(r.text)
        self.assertEqual(obj['data']['roles'], None)

    # 获取用户信息
    def test_getUserInfo(self):
        r = requests.post(URL + '/api/v1/admin/user/create?permission=chef',
                          headers={"token": "123"})
        obj = json.loads(r.text)
        self.assertEqual(obj['data']['roles'], "chef")
        self.assertEqual(obj['data']['name'], "ceobe")

    # 修改用户名
    def test_changeUsername(self):
        loginr = requests.post(URL + '/api/v1/admin/user/login',
                          json={"username" : self.newerChefUsername,
                                "password" : self.newerChefPassword})
        obj = json.loads(loginr.text)
        chefToken = obj['data']['token']
        r = requests.post(URL + '/api/v1/admin/user/changeUsername',
                          headers={"token": chefToken},
                          json={"username": "newChef"})
        obj = json.loads(r.text)
        self.assertEqual(obj['username'], "newChef")
        self.newerChefUsername="newChef"

    # # 修改密码
    # def test_changePassword(self):
    #     loginr = requests.post(URL + '/api/v1/admin/user/login',
    #                       json={"username" : self.newerChefUsername,
    #                             "password" : self.newerChefPassword})
    #     obj = json.loads(loginr.text)
    #     chefToken = obj['data']['token']
    #     r = requests.post(URL + '/api/v1/admin/user/changeUsername',
    #                       headers={"token": chefToken},
    #                       json={"old_password":,
    #                               "new_password:"})

if __name__ == '__main__' :
    unittest.main()
