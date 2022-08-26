import unittest
import requests
import json
import hashlib

URL = 'http://127.0.0.1:8000/api/v1'

# 每次测试时务必更换request body内容 or会得到C0000B版本存在
# 针对资源模块的测试
class Resource_Module(unittest.TestCase) :
    initialUsername="ceobe"
    initialPassword="fdb04988b4e48c4f16952457e86b8d25"
    initialToken="eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwibnVtX3B3ZF9jaGFuZ2UiOjB9.Le2vog19Tq5tPV6h082HX4dZakYiI7eU4huxe0GfRh8"
    architectUsername = "testarchitect"
    architectPassword = "K5SJl8WbWz"
    cookerUsername = "testcooker"
    cookerPassword = "VTbXkp1AGd"
    chefUsername = "testchef"
    chefPassword = "0abtxnRZ8F"

    def login_getToken(self,username,password):
        loginr = requests.post(URL + '/admin/user/login',
                          json={"username" : username,
                                "password" : password})
        obj = json.loads(loginr.text)
        if (obj['code']==None):
            print("\nlogin successfully\n")
            print(obj['data']['token'])
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

    # 上传资源内容
    def test_uploadResource_chef(self):
        r=requests.post(URL+"/admin/resource/submitList",
                        headers= {"token": self.initialToken},
                        json={
    "resources": {
        "start_time":"2021-11-22 16:00:00",
        "over_time":"2021-12-06 03:59:59"

},
    "countdown": [
        {
            "text": "当前轮换池结束",
            "remark": "刻俄柏[兑换],水月,赤冬,莱恩哈特[ 兑换],安哲拉",
            "time": "2022-02-17 03:59:59",
            "start_time": "2022-02-03 04:00:00",
            "over_time": "2022-02-17 03:59:59"
        },
        {
            "text": "当前轮换池结束",
            "remark": "棘刺[兑换]、艾雅法拉、乌有、诗怀雅[兑换]、雷蛇",
            "time": "2022-02-03 03:59:59",
            "start_time": "2022-01-20 04:00:00",
            "over_time": "2022-02-03 03:59:59"
        }
    ]
})
        obj=json.loads(r.text)
        assert obj['code'] is None

    def test_uploadResource_cooker(self) :
        token=self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        r = requests.post(URL + "/admin/resource/submitList",
                              headers={"token" : token},
                              json={
                                  "resources" : {
                                      "start_time" : "2021-11-22 16:00:00",
                                      "over_time" : "2021-12-06 03:59:59"

                                  },
                                  "countdown" : [
                                      {
                                          "text" : "当前轮换池结束",
                                          "remark" : "刻俄柏[兑换],水月,赤冬,莱恩哈特[ 兑换],安哲拉",
                                          "time" : "2022-02-17 03:59:59",
                                          "start_time" : "2022-02-03 04:00:00",
                                          "over_time" : "2022-02-17 03:59:59"
                                      },
                                      {
                                          "text" : "当前轮换池结束",
                                          "remark" : "棘刺[兑换]、艾雅法拉、乌有、诗怀雅[兑换]、雷蛇",
                                          "time" : "2022-02-03 03:59:59",
                                          "start_time" : "2022-01-20 04:00:00",
                                          "over_time" : "2022-02-03 03:59:59"
                                      }
                                  ]
                              })
        obj = json.loads(r.text)
        assert obj['code'] is None

    def test_uploadResource_architect(self) :
        token=self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r = requests.post(URL + "/admin/resource/submitList",
                              headers={"token" : token},
                              json={
                                  "resources" : {
                                      "start_time" : "2021-11-22 16:00:00",
                                      "over_time" : "2021-12-06 03:59:59"

                                  },
                                  "countdown" : [
                                      {
                                          "text" : "当前轮换池结束",
                                          "remark" : "刻俄柏[兑换],水月,赤冬,莱恩哈特[ 兑换],安哲拉",
                                          "time" : "2022-02-17 03:59:59",
                                          "start_time" : "2022-02-03 04:00:00",
                                          "over_time" : "2022-02-17 03:59:59"
                                      },
                                      {
                                          "text" : "当前轮换池结束",
                                          "remark" : "棘刺[兑换]、艾雅法拉、乌有、诗怀雅[兑换]、雷蛇",
                                          "time" : "2022-02-03 03:59:59",
                                          "start_time" : "2022-01-20 04:00:00",
                                          "over_time" : "2022-02-03 03:59:59"
                                      }
                                  ]
                              })
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], "A0002")

        # 获取资源内容
    def test_getResourceList_chef(self):
        r=requests.get(URL+'/admin/resource/list',
                       headers={"token":self.initialToken})
        obj=json.loads(r.text)
        assert obj['code'] is None

    def test_getResourceList_cooker(self):
        r=requests.get(URL+'/admin/resource/list',
                       headers={"token":self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))})
        obj=json.loads(r.text)
        assert obj['code'] is None

    def test_getResourceList_architect(self):
        r=requests.get(URL+'/admin/resource/list',
                       headers={"token":self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'] , "A0002")
if __name__ =='__main__':
    unittest.main()