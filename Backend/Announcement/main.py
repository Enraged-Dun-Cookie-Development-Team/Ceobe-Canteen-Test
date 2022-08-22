import unittest
import requests
import json

URL = 'http://127.0.0.1:8000'

# 针对公告模块的测试
class Announcement_Module(unittest.TestCase) :
    initialUsername="ceobe"
    initialPassword="fdb04988b4e48c4f16952457e86b8d25"

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

    # 上传公告测试
    def test_uploadAnnouncement(self):
        token=self.login_getToken(self.initialUsername,self.initialPassword)
        r=requests.post(URL+ '/admin/announcement/submitList',
                        headers={"token": token},
                        json=[
	{
		"start_time": "2022-02-15 16:00:00",
		"over_time": "2022-02-22 03:59:59",
		"img_url": "icon",
		"content": "<p><font color=\"#e03b3b\">故事集「阴云火花」</font>将 于<font color=\"#ffba4b\">2月22号</font>结束</p><p>结束时间为<font color=\"#ffba4b\">周二4:00</font></p><p>活动期间掉落<font color=\"#e4d64a\">聚酸酯组</font>、<font color=\"#e4d64a\">晶体元件</font></p><p>活动开启时，快捷链接更新作业视频</p><p>或者点击 <drawer>这里</drawer> 快速跳转</p>",
		"notice": "false"
	},
	{
		"start_time": "2022-02-22 04:00:00",
		"over_time": "2022-02-22 15:59:59",
		"img_url": "https://ak.hycdn.cn/announce/images/20220125/e11f6c95958d685bbbedfd0fd799755a.JPG",
		"content": "<p><u>故事集「阴云火花」</u>将于<strike>22号</strike>结束</p><p><span style=\"background-color: rgb(228, 214, 74);\">21号的周一</span>别急着刷剿灭，等活动结束再刷</p><p>虽然是故事集，但是掉率也比主线高</p><p>理智尽量留给<i>活动</i></p><p>下个活动是<b>危机合约</b></p>",
		"notice": "true"
	},
	{
		"start_time": "2022-02-15 04:00:00",
		"over_time": "2033-05-28 00:00:00",
		"img_url": "icon",
		"content": "<p>博士，谢谢你使用蹲饼。</p><p>如果觉得好用的话，希望能去<a href=\"https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue\" target=\"_blank\" one-link-mark=\"yes\">GitHub</a>上点个Star或者</p><p>去<a href=\"https://chrome.google.com/webstore/detail/%E8%B9%B2%E9%A5%BC-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cook/gblmdllhbodefkmimbcjpflhjneagkkd?hl=zh-CN\" target=\"_blank\" one-link-mark=\"yes\">Chrome商店</a> ，<a href=\"https://microsoftedge.microsoft.com/addons/detail/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknight/jimmfliacfpeabcifcghmdankmdnmfmn?hl=zh-CN\" target=\"_blank\" one-link-mark=\"yes\">Edge商店</a>或<a href=\"https://addons.mozilla.org/zh-CN/firefox/addon/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cookies/\" target=\"_blank\" one-link-mark=\"yes\">Firefox商 店</a>里面给个好评</p><p>也可以去<a href=\"https://arknightscommunity.drblack-system.com/15386.html\" target=\"_blank\" one-link-mark=\"yes\">泰拉通讯枢纽</a>里面回复我们，或者去<a href=\"https://www.bilibili.com/video/BV1jv411P7bR/\" target=\"_blank\" one-link-mark=\"yes\">b 站视频</a>给个三连</p><p>欢迎加群<a href=\"https://jq.qq.com/?_wv=1027&amp;k=Vod1uO13\" target=\"_blank\" one-link-mark=\"yes\">【蹲饼测试群】</a>一起聊天， 蹲饼！</p>",
		"notice": "false"
	}
])
        obj=json.loads(r.text)
        if(obj['code'] is not "20000"):
            print (obj)
        assert obj['code'] is "20000"

    # 获取公告测试
    def test_getAnnouncemnet(self):
        token=self.login_getToken(self.initialUsername,self.initialPassword)
        r=requests.get(URL+ '/admin/announcement/get',
                        headers={"token": token})
        obj=json.loads(r.text)
        if(obj['code'] is not "T2000"):
            print (obj)
        assert obj['code'] is "T2000"








if __name__ == '__main__' :
    unittest.main()