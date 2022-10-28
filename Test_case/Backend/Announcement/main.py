import unittest
import requests
import json
import hashlib

URL = 'http://127.0.0.1:8000/api/v1'

initialUsername = "ceobe"
initialPassword = "fdb04988b4e48c4f16952457e86b8d25"
architectUsername = "testarchitect"
architectPassword = "K5SJl8WbWz"
cookerUsername = "testcooker"
cookerPassword = "VTbXkp1AGd"
chefUsername = "testchef"
chefPassword = "0abtxnRZ8F"
chefUsername = "testchef"
chefPassword = "0abtxnRZ8F"
#
# 针对公告模块的测试
class Announcement_Module(unittest.TestCase) :

    def login_getToken(self,username,password):
        loginr = requests.post(URL + '/admin/user/login',
                          json={"username" : username,
                                "password" : password})
        obj = json.loads(loginr.text)
        if (obj['code']==None):
            print("login successfully")
            return obj['data']['token']
        else:
            print('login failed error Code:'+obj['code'])

    def list_dumps(self,list):
        for i in list:
            i=json.dumps(i,ensure_ascii=False)
        return list

    #md5 加密
    def exchange_to_md5(self, content) :
        # 创建md5对象
        md_obj = hashlib.md5()
        # 传入信息进行加密，注意传入的信息必须进行encode编码，否则报错
        md_obj.update(content.encode("utf-8"))
        # 获取加密后的信息
        md_res = md_obj.hexdigest()
        return md_res

    # 上传公告测试:chef
    def test_uploadAnnouncement_chef(self):
        token=self.login_getToken(chefUsername,self.exchange_to_md5(chefPassword))
        data=[{
   "start_time": "2022-02-15 16:00:00",
   "over_time": "2022-02-22 03:59:59",
   "img_url": "icon",
   "content": "<p><font color=\"#e03b3b\">故事集「阴云火花」</font>将 于<font color=\"#ffba4b\">2月22号</font>结束</p><p>结束时间为<font color=\"#ffba4b\">周二4:00</font></p><p>活动期间掉落<font color=\"#e4d64a\">聚酸酯组</font>、<font color=\"#e4d64a\">晶体元件</font></p><p>活动开启时，快捷链接更新作业视频</p><p>或者点击 <drawer>这里</drawer> 快速跳转</p>",
   "notice": False
}]
        r=requests.post(URL+ '/admin/announcement/submitList',
                        headers={"token": token},
                        json=self.list_dumps(data))
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],None)

    def test_uploadAnnouncement_chef(self) :
        token = self.login_getToken(chefUsername, self.exchange_to_md5(chefPassword))
        data = [{
            "start_time" : "2022-02-15 16:00:00",
            "over_time" : "2022-02-22 03:59:59",
            "img_url" : "icon",
            "content" : "<p><font color=\"#e03b3b\">故事集「阴云火花」</font>将 于<font color=\"#ffba4b\">2月22号</font>结束</p><p>结束时间为<font color=\"#ffba4b\">周二4:00</font></p><p>活动期间掉落<font color=\"#e4d64a\">聚酸酯组</font>、<font color=\"#e4d64a\">晶体元件</font></p><p>活动开启时，快捷链接更新作业视频</p><p>或者点击 <drawer>这里</drawer> 快速跳转</p>",
            "notice" : False
        }]
        r = requests.post(URL + '/admin/announcement/submitList',
                          headers={"token" : token},
                          json=self.list_dumps(data))
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], None)

        # 上传公告测试:cooker
    def test_uploadAnnouncement_cooker(self) :
        token = self.login_getToken(cookerUsername, self.exchange_to_md5(cookerPassword))
        data = [{
                "start_time" : "2022-02-15 16:00:00",
                "over_time" : "2022-02-22 03:59:59",
                "img_url" : "icon",
                "content" : "<p><font color=\"#e03b3b\">故事集「阴云火花」</font>将 于<font color=\"#ffba4b\">2月22号</font>结束</p><p>结束时间为<font color=\"#ffba4b\">周二4:00</font></p><p>活动期间掉落<font color=\"#e4d64a\">聚酸酯组</font>、<font color=\"#e4d64a\">晶体元件</font></p><p>活动开启时，快捷链接更新作业视频</p><p>或者点击 <drawer>这里</drawer> 快速跳转</p>",
                "notice" : False
        }]
        r = requests.post(URL + '/admin/announcement/submitList',
                              headers={"token" : token},
                              json=self.list_dumps(data))
        obj = json.loads(r.text)
        assert obj['code'] is None

    # 上传公告测试:architect 无权限
    def test_uploadAnnouncement_architect(self) :
        token = self.login_getToken(architectUsername, self.exchange_to_md5(architectPassword))
        data = {
            "start_time" : "2022-02-15 16:00:00",
            "over_time" : "2022-02-22 03:59:59",
            "img_url" : "icon",
            "content" : "<p><font color=\"#e03b3b\">故事集「阴云火花」</font>将 于<font color=\"#ffba4b\">2月22号</font>结束</p><p>结束时间为<font color=\"#ffba4b\">周二4:00</font></p><p>活动期间掉落<font color=\"#e4d64a\">聚酸酯组</font>、<font color=\"#e4d64a\">晶体元件</font></p><p>活动开启时，快捷链接更新作业视频</p><p>或者点击 <drawer>这里</drawer> 快速跳转</p>",
            "notice" : False
        }
        r = requests.post(URL + '/admin/announcement/submitList',
                              headers={"token" : token},
                              json=json.dumps(data))
        obj = json.loads(r.text)
        self.assertEqual(obj['code'],"A0002")
    # 获取公告测试
    def test_getAnnouncemnet_chef(self):
        token=self.login_getToken(initialUsername,initialPassword)
        r=requests.get(URL+ '/admin/announcement/get',
                        headers={"token": token})
        obj=json.loads(r.text)
        assert obj['code'] is None

    def test_getAnnouncemnet_cooker(self):
        token=self.login_getToken(cookerUsername,self.exchange_to_md5(cookerPassword))
        r=requests.get(URL+ '/admin/announcement/get',
                        headers={"token": token})
        obj=json.loads(r.text)
        assert obj['code'] is None

    def test_getAnnouncemnet_architect(self):
        token=self.login_getToken(architectUsername,self.exchange_to_md5(architectPassword))
        r=requests.get(URL+ '/admin/announcement/get',
                        headers={"token": token})
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],"A0002")



if __name__ == '__main__' :
    unittest.main()