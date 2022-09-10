import unittest
import requests
import json
import hashlib

URL = 'http://127.0.0.1:8000/api/v1'
# 每次记得更改id十分位
id_chef = "20.4"
id_cooker = "30.4"
id_architect = "40.4"
data = {
    "id": "18.8",
    "description": "",
    "cv_link": "",
    "fraction": 1,
    "daily": [
        {
            "datetime": "2022-06-16",
            "info": [
                {
                    "forecast_status": "true",
                    "forecast": "<签到服饰>“待晴日”- 深靛"
                },
                {
                    "forecast_status": "true",
                    "forecast": "<签到家具>“ 山中弈 ”&“ 亭上雪"
                }
            ],
            "content": "<p>第一天<font color=\"#fdbf22\">平<i>稳落</i>地</font>，不<b>愧</b>是无敌的<strike>banana</strike>老师</p><p>不负<u>饼学大厦</u>的名号，我们的<span style=\"background-color: rgb(224, 59, 59);\">未来一片光明</span>！（挥拳）<span style=\"font-size: 14px;\">😀</span></p>"
        },
        {
            "datetime": "2022-01-17",
            "info": [
                {
                    "forecast_status": "true",
                    "forecast": "<活动异格>五星速射手 -寒芒克洛丝"
                },
                {
                    "forecast_status": "false",
                    "forecast": "“且试箸”- 食铁兽"
                }
            ],
            "content": "<p>第二天瞬间垮掉，不愧是笨蛋的banana老师</p><p>有愧饼学大厦的名号，我们的未来一片黑暗！（挥泪）</p>"
        },
        {
            "datetime": "2022-01-18",
            "info": [
                {
                    "forecast_status": "true",
                    "forecast": "五星战术家 - 夜半"
                },
                {
                    "forecast_status": "false",
                    "forecast": "【常驻标准寻访预告】"
                }
            ],
            "content": "<p>第三天\\n请在此处填写今日感想\\n第一句，第二句</p><p>第三句，第四句！（挥【填写物品名称】）</p><p>（干员按正常顺序发布，轮换池提前一天芭娜娜没想到）</p>"
        },
        {
            "datetime": "2022-01-19",
            "info": [
                {
                    "forecast_status": "true",
                    "forecast": "闪断更新公告"
                },
                {
                    "forecast_status": "true",
                    "forecast": " “冷山 月” - 乌有"
                }
            ],
            "content": "<p>第四天锟斤拷，不愧是锟斤拷的banana老师</p><p>锟斤拷锟斤拷的名号，我们的未来一片烫烫烫！</p>"
        },
        {
            "datetime": "2022-01-21",
            "info": [
                {
                    "forecast_status": "false",
                    "forecast": "“染尘烟” - 夕"
                }
            ],
            "content": "<p>芭娜娜今天做出以下锐评：</p><p>“嘿嘿，夕我的夕”</p>"
        },
        {
            "datetime": "2022-01-22",
            "info": [
                {
                    "forecast_status": "true",
                    "forecast": "#罗 德岛闲逛部#"
                },
                {
                    "forecast_status": "true",
                    "forecast": "六星行商 - 老鲤"
                }
            ],
            "content": "<p>没想到吧其他啥也没有了【抹眼泪】</p>"
        },
        {
            "datetime": "2022-01-23",
            "info": [
                {
                    "forecast_status": "true",
                    "forecast": "#罗德岛相簿#"
                },
                {
                    "forecast_status": "true",
                    "forecast": "六星召唤师 - 令 [限定]"
                },
                {
                    "forecast_status": "true",
                    "forecast": "【山城茶馆】主题家具"
                }
            ],
            "content": "<p>#明日方舟##饼学大厦#&nbsp;</p><p>世界未解之谜之一被解开了：</p><p>昨天不发饼的原因是</p><p>从暮落开始YJ有意更新干员基建/技能介绍的动图的新样式（每年一次）</p>"
        },
        {
            "datetime": "2022-01-25",
            "info": [
                {
                    "forecast_status": "unknown",
                    "forecast": "令EP"
                },
                {
                    "forecast_status": "unknown",
                    "forecast": "Sidestory「将进酒」开启"
                }
            ],
            "content": ""
        },
        {
            "datetime": "2022-01-26",
            "info": [
                {
                    "forecast_status": "unknown",
                    "forecast": "老鲤EP"
                }
            ],
            "content": ""
        },
        {
            "datetime": "2022-01-30",
            "info": [
                {
                    "forecast_status": "unknown",
                    "forecast": "#罗德岛相簿#（可能延后至02.01）"
                }
            ],
            "content": ""
        },
        {
            "datetime": "2022-02-01",
            "info": [
                {
                    "forecast_status": "unknown",
                    "forecast": "春节贺图"
                }
            ],
            "content": ""
        }
    ]
}

#
# 针对饼学大厦模块的测试
class Mansion_Module(unittest.TestCase) :
    initialUsername="ceobe"
    initialPassword="fdb04988b4e48c4f16952457e86b8d25"
    initialToken="eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwibnVtX3B3ZF9jaGFuZ2UiOjB9.Le2vog19Tq5tPV6h082HX4dZakYiI7eU4huxe0GfRh8"
    architectUsername = "testarchitect"
    architectPassword = "K5SJl8WbWz"
    cookerUsername = "testcooker"
    cookerPassword = "VTbXkp1AGd"
    chefUsername = "testchef"
    chefPassword = "0abtxnRZ8F"
    def login_getToken(self, username, password) :
        loginr = requests.post(URL + '/admin/user/login',
                               json={"username" : username,
                                     "password" : password})
        obj = json.loads(loginr.text)
        if (obj['code'] == None) :
            print("\nlogin successfully\n")
            print(obj['data']['token'])
            return obj['data']['token']
        else :
            print('login failed error Code:' + obj['code'])

    # md5 加密
    def exchange_to_md5(self, content) :
        # 创建md5对象
        md_obj = hashlib.md5()
        # 传入信息进行加密，注意传入的信息必须进行encode编码，否则报错
        md_obj.update(content.encode("utf-8"))
        # 获取加密后的信息
        md_res = md_obj.hexdigest()
        return md_res

    def mansion_dumps(self,mansion):
        for content in mansion:
            content=json.dumps(content,ensure_ascii=False)
        print(mansion)
        return mansion

    # id修改
    def id_edit(self,data,id) :
        data['id'] = id
        return data

    @classmethod
    def setUpClass(cls):
        chef_data=cls.id_edit(cls,data,"10.1")
        r=requests.post(URL+'/admin/mansion/upload',
                        headers={"token":cls.initialToken},
                        json=chef_data)
        cooker_data=cls.id_edit(cls,data,"10.2")
        r=requests.post(URL+'/admin/mansion/upload',
                        headers={"token":cls.initialToken},
                        json=cooker_data)
        architect_data=cls.id_edit(cls,data,"10.3")
        r=requests.post(URL+'/admin/mansion/upload',
                        headers={"token":cls.initialToken},
                        json=architect_data)



    # 上传大厦信息
    # 加id参数为修改 不加为新建
    def test_uploadMansion_chef(self):
        test_data=self.id_edit(data,id_chef)
        r=requests.post(URL+'/admin/mansion/upload',
                        headers={"token":self.initialToken},
                        json=test_data)
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

    def test_repeat_uploadMansion_chef(self) :
        test_data = self.id_edit(data, "18.6")
        r = requests.post(URL + '/admin/mansion/upload',
                          headers={"token" : self.initialToken},
                          json=test_data)
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], 'C0008')

    def test_uploadMansion_architect(self):
        test_data=self.id_edit(data,id_architect)
        token=self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r=requests.post(URL+'/admin/mansion/upload',
                        headers={"token":token},
                        json=test_data)
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

    def test_repeat_uploadMansion_architect(self):
        test_data=self.id_edit(data,"18.6")
        token=self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r=requests.post(URL+'/admin/mansion/upload',
                        headers={"token":token},
                        json=test_data)
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],'C0008')

    def test_uploadMansion_cooker(self):
        test_data=self.id_edit(data,id_cooker)
        token=self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        r=requests.post(URL+'/admin/mansion/upload',
                        headers={"token":token},
                        json=test_data)
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],'A0002')

    def test_repeat_uploadMansion_cooker(self):
        test_data=self.id_edit(data,"18.6")
        token=self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        r=requests.post(URL+'/admin/mansion/upload',
                        headers={"token":token},
                        json=test_data)
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],'A0002')

    # 修改大厦
    def test_editMansion_chef(self):
        test_data=self.id_edit(data,"18.6")
        r=requests.post(URL+'/admin/mansion/upload?idBefore=18.6',
                        headers={"token":self.initialToken},
                        json=test_data)
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

    def test_editMansion_architect(self):
        test_data=self.id_edit(data,"18.6")
        token=self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r=requests.post(URL+'/admin/mansion/upload?idBefore=18.6',
                        headers={"token":token},
                        json=test_data)
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

    def test_editMansion_cooker(self):
        test_data=self.id_edit(data,"18.6")
        token=self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        r=requests.post(URL+'/admin/mansion/upload?idBefore=18.6',
                        headers={"token":token},
                        json=test_data)
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],'A0002')

    # 获取大厦信息
    def test_getMansionId_chef(self):
        r=requests.get(URL+'/admin/mansion/getId',
                        headers={"token": self.initialToken})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

    def test_getMansionId_architect(self):
        token=self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r=requests.get(URL+'/admin/mansion/getId',
                        headers={"token": token})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

    def test_getMansionId_cooker(self):
        token=self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        r=requests.get(URL+'/admin/mansion/getId',
                        headers={"token": token})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],'A0002')

    # 获取最近大厦号
    def test_getMansionInfo_chef(self):
        r=requests.get(URL+'/admin/mansion/getInfo?mansion_id=18.6',
                        headers={"token":self.initialToken})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

    def test_getMansionInfo_cooker(self):
        r=requests.get(URL+'/admin/mansion/getInfo?mansion_id=18.6',
                        headers={"token":self.initialToken})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

    def test_getMansionInfo_architect(self):
        token = self.login_getToken(self.architectUsername, self.exchange_to_md5(self.architectPassword))
        r=requests.get(URL+'/admin/mansion/getInfo?mansion_id=18.6',
                        headers={"token":token})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

#    删除大厦
    def test_deleteMansion_chef(self):
        r=requests.get(URL+'/admin/mansion/getInfo?mansion_id=10.1',
                        headers={"token":self.initialToken})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

    def test_deleteMansion_cooker(self):
        token=self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        r=requests.get(URL+'/admin/mansion/getInfo?mansion_id=10.2',
                        headers={"token":token})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],'A0002')

    def test_deleteMansion_architect(self):
        token=self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r=requests.get(URL+'/admin/mansion/getInfo?mansion_id=10.3',
                        headers={"token":token})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)



if __name__ == '__main__' :
    unittest.main()