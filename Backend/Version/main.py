import unittest
import requests
import json
import hashlib

URL = 'http://127.0.0.1:8000/api/v1'

# 每次记得改变version参数
version_a = "5.2.2"
version_b = "5.3.2"
version_c = "5.4.2"
version_d = "0.2.2"
version_e = "0.3.2"
version_f = "0.4.2"

# 针对版本模块的测试
class Version_Module(unittest.TestCase) :

    initialUsername="ceobe"
    initialPassword="fdb04988b4e48c4f16952457e86b8d25"
    initialToken="eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwibnVtX3B3ZF9jaGFuZ2UiOjB9.Le2vog19Tq5tPV6h082HX4dZakYiI7eU4huxe0GfRh8"
    architectUsername = "testarchitect"
    architectPassword = "K5SJl8WbWz"
    architectToken="eyJhbGciOiJIUzI1NiJ9.eyJpZCI6NzYsIm51bV9wd2RfY2hhbmdlIjowfQ.JX83zw9HBMd9aQvV3YLsbDmmDsQC4g5USgAkMVAOxPc"
    cookerUsername = "testcooker"
    cookerPassword = "VTbXkp1AGd"
    cookerToken="eyJhbGciOiJIUzI1NiJ9.eyJpZCI6NzcsIm51bV9wd2RfY2hhbmdlIjowfQ.309KM9hd6l_R5UmFFxIO-UHb17oO5ydHphQ8sORJpcE"
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

    def list_dumps(self,list):
        for i in list:
            i=json.dumps(i,ensure_ascii=False)
        return list

    # 上传插件版本
    # 正常情况
    def test_uploadPlugin_common_chef(self):
        r=requests.post(URL+'/admin/version/plugin',
                       headers={"token":self.initialToken},
                       json={
	"version": version_a,
	"title": "小刻食堂翻新啦 - 3.0.14",
	"description": "   🎉 升级企鹅物流数据相关，优化蹲饼逻辑，修复若干bug\n\n    1.企鹅物流数据样式更加直观\n    2.企鹅物流数据可选按百分比掉落排序或单件期望理智排序\n    3.关闭企鹅物流数据提醒\n    4.优化蹲饼频率逻辑，蹲饼永不被ban\n    5.修复打开列表频繁跳出游戏内版本更新通知\n    6.修 复火狐浏览器无法进行生成图片并复制 (需要配置一些东西，具体看火狐安装方法部分)\n    7.优化生成图片并复制的速度\n    8.优化更新配置，避免无意义请求",
	"down": {
		"crx": "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.crx",
		"zip": "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.zip",
		"spare": ["https://pan.baidu.com/s/1kzY6kpfYqLcGpuaiwQOGoA", "备用下载（提取码 jzq9）"],
		"chrome": "https://chrome.google.com/webstore/detail/%E8%B9%B2%E9%A5%BC-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cook/gblmdllhbodefkmimbcjpflhjneagkkd?hl=zh-CN",
		"edge": "https://microsoftedge.microsoft.com/addons/detail/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknight/jimmfliacfpeabcifcghmdankmdnmfmn?hl=zh-CN",
		"firefox": "https://addons.mozilla.org/zh-CN/firefox/addon/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cookies/"
	}
})
        obj=json.loads(r.text)
        assert obj['code'] is None

    def test_uploadPlugin_common_cooker(self) :
        token=self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        r = requests.post(URL + '/admin/version/plugin',
                          headers={"token" : token},
                          json={
                              "version" : version_b,
                              "title" : "小刻食堂翻新啦 - 3.0.14",
                              "description" : "   🎉 升级企鹅物流数据相关，优化蹲饼逻辑，修复若干bug\n\n    1.企鹅物流数据样式更加直观\n    2.企鹅物流数据可选按百分比掉落排序或单件期望理智排序\n    3.关闭企鹅物流数据提醒\n    4.优化蹲饼频率逻辑，蹲饼永不被ban\n    5.修复打开列表频繁跳出游戏内版本更新通知\n    6.修 复火狐浏览器无法进行生成图片并复制 (需要配置一些东西，具体看火狐安装方法部分)\n    7.优化生成图片并复制的速度\n    8.优化更新配置，避免无意义请求",
                              "down" : {
                                  "crx" : "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.crx",
                                  "zip" : "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.zip",
                                  "spare" : ["https://pan.baidu.com/s/1kzY6kpfYqLcGpuaiwQOGoA", "备用下载（提取码 jzq9）"],
                                  "chrome" : "https://chrome.google.com/webstore/detail/%E8%B9%B2%E9%A5%BC-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cook/gblmdllhbodefkmimbcjpflhjneagkkd?hl=zh-CN",
                                  "edge" : "https://microsoftedge.microsoft.com/addons/detail/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknight/jimmfliacfpeabcifcghmdankmdnmfmn?hl=zh-CN",
                                  "firefox" : "https://addons.mozilla.org/zh-CN/firefox/addon/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cookies/"
                              }
                          })
        obj=json.loads(r.text)
        assert obj['code'] is None
        
    def test_uploadPlugin_common_architect(self) :
        token=self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r = requests.post(URL + '/admin/version/plugin',
                          headers={"token" : token},
                          json={
                              "version" : version_c,
                              "title" : "小刻食堂翻新啦 - 3.0.14",
                              "description" : "   🎉 升级企鹅物流数据相关，优化蹲饼逻辑，修复若干bug\n\n    1.企鹅物流数据样式更加直观\n    2.企鹅物流数据可选按百分比掉落排序或单件期望理智排序\n    3.关闭企鹅物流数据提醒\n    4.优化蹲饼频率逻辑，蹲饼永不被ban\n    5.修复打开列表频繁跳出游戏内版本更新通知\n    6.修 复火狐浏览器无法进行生成图片并复制 (需要配置一些东西，具体看火狐安装方法部分)\n    7.优化生成图片并复制的速度\n    8.优化更新配置，避免无意义请求",
                              "down" : {
                                  "crx" : "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.crx",
                                  "zip" : "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.zip",
                                  "spare" : ["https://pan.baidu.com/s/1kzY6kpfYqLcGpuaiwQOGoA", "备用下载（提取码 jzq9）"],
                                  "chrome" : "https://chrome.google.com/webstore/detail/%E8%B9%B2%E9%A5%BC-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cook/gblmdllhbodefkmimbcjpflhjneagkkd?hl=zh-CN",
                                  "edge" : "https://microsoftedge.microsoft.com/addons/detail/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknight/jimmfliacfpeabcifcghmdankmdnmfmn?hl=zh-CN",
                                  "firefox" : "https://addons.mozilla.org/zh-CN/firefox/addon/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cookies/"
                              }
                          })
        obj=json.loads(r.text)
        self.assertEqual(obj['code'], "A0002")


    # 重复版本情况
    def test_uploadPlugin_repeated_chef(self):
        r = requests.post(URL + '/admin/version/plugin',
                          headers={"token" : self.initialToken},
                          json={
                              "version" : "5.0.0",
                              "title" : "小刻食堂翻新啦 - 3.0.14",
                              "description" : "   🎉 升级企鹅物流数据相关，优化蹲饼逻辑，修复若干bug\n\n    1.企鹅物流数据样式更加直观\n    2.企鹅物流数据可选按百分比掉落排序或单件期望理智排序\n    3.关闭企鹅物流数据提醒\n    4.优化蹲饼频率逻辑，蹲饼永不被ban\n    5.修复打开列表频繁跳出游戏内版本更新通知\n    6.修 复火狐浏览器无法进行生成图片并复制 (需要配置一些东西，具体看火狐安装方法部分)\n    7.优化生成图片并复制的速度\n    8.优化更新配置，避免无意义请求",
                              "down" : {
                                  "crx" : "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.crx",
                                  "zip" : "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.zip",
                                  "spare" : ["https://pan.baidu.com/s/1kzY6kpfYqLcGpuaiwQOGoA", "备用下载（提取码 jzq9）"],
                                  "chrome" : "https://chrome.google.com/webstore/detail/%E8%B9%B2%E9%A5%BC-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cook/gblmdllhbodefkmimbcjpflhjneagkkd?hl=zh-CN",
                                  "edge" : "https://microsoftedge.microsoft.com/addons/detail/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknight/jimmfliacfpeabcifcghmdankmdnmfmn?hl=zh-CN",
                                  "firefox" : "https://addons.mozilla.org/zh-CN/firefox/addon/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cookies/"
                              }
                          })
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], "C000B")

    def test_uploadPlugin_repeated_cooker(self):
        token=self.login_getToken(self.cookerUsername,self.exchange_to_md5(self.cookerPassword))
        print(token)
        r = requests.post(URL + '/admin/version/plugin',
                          headers={"token" : token},
                          json={
                              "version" : "5.0.0",
                              "title" : "小刻食堂翻新啦 - 3.0.14",
                              "description" : "   🎉 升级企鹅物流数据相关，优化蹲饼逻辑，修复若干bug\n\n    1.企鹅物流数据样式更加直观\n    2.企鹅物流数据可选按百分比掉落排序或单件期望理智排序\n    3.关闭企鹅物流数据提醒\n    4.优化蹲饼频率逻辑，蹲饼永不被ban\n    5.修复打开列表频繁跳出游戏内版本更新通知\n    6.修 复火狐浏览器无法进行生成图片并复制 (需要配置一些东西，具体看火狐安装方法部分)\n    7.优化生成图片并复制的速度\n    8.优化更新配置，避免无意义请求",
                              "down" : {
                                  "crx" : "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.crx",
                                  "zip" : "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.zip",
                                  "spare" : ["https://pan.baidu.com/s/1kzY6kpfYqLcGpuaiwQOGoA", "备用下载（提取码 jzq9）"],
                                  "chrome" : "https://chrome.google.com/webstore/detail/%E8%B9%B2%E9%A5%BC-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cook/gblmdllhbodefkmimbcjpflhjneagkkd?hl=zh-CN",
                                  "edge" : "https://microsoftedge.microsoft.com/addons/detail/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknight/jimmfliacfpeabcifcghmdankmdnmfmn?hl=zh-CN",
                                  "firefox" : "https://addons.mozilla.org/zh-CN/firefox/addon/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cookies/"
                              }
                          })
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], "C000B")

    def test_uploadPlugin_repeated_architect(self):
        token=self.login_getToken(self.architectUsername,self.exchange_to_md5(self.architectPassword))
        r = requests.post(URL + '/admin/version/plugin',
                          headers={"token" : token},
                          json={
                              "version" : "5.0.0",
                              "title" : "小刻食堂翻新啦 - 3.0.14",
                              "description" : "   🎉 升级企鹅物流数据相关，优化蹲饼逻辑，修复若干bug\n\n    1.企鹅物流数据样式更加直观\n    2.企鹅物流数据可选按百分比掉落排序或单件期望理智排序\n    3.关闭企鹅物流数据提醒\n    4.优化蹲饼频率逻辑，蹲饼永不被ban\n    5.修复打开列表频繁跳出游戏内版本更新通知\n    6.修 复火狐浏览器无法进行生成图片并复制 (需要配置一些东西，具体看火狐安装方法部分)\n    7.优化生成图片并复制的速度\n    8.优化更新配置，避免无意义请求",
                              "down" : {
                                  "crx" : "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.crx",
                                  "zip" : "https://github.com/Enraged-Dun-Cookie-Development-Team/Dun-Cookie-Vue/releases/download/3.0.14/Dun-Cookie-3.0.14.zip",
                                  "spare" : ["https://pan.baidu.com/s/1kzY6kpfYqLcGpuaiwQOGoA", "备用下载（提取码 jzq9）"],
                                  "chrome" : "https://chrome.google.com/webstore/detail/%E8%B9%B2%E9%A5%BC-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cook/gblmdllhbodefkmimbcjpflhjneagkkd?hl=zh-CN",
                                  "edge" : "https://microsoftedge.microsoft.com/addons/detail/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknight/jimmfliacfpeabcifcghmdankmdnmfmn?hl=zh-CN",
                                  "firefox" : "https://addons.mozilla.org/zh-CN/firefox/addon/%E5%B0%8F%E5%88%BB%E9%A3%9F%E5%A0%82-%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%E8%B9%B2%E9%A5%BC%E5%99%A8-arknights-cookies/"
                              }
                          })
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], "A0002")

    # 上传app版本
    # 正常鉴权
    def test_uploadApp_common_chef(self):
        content={
        "version": version_d,
        "force": True,
        "last_force_version": "0.0.1",
        "description": "修改界面布局\n启用蜜饼工坊测试样本"
        }
        r=requests.post(URL+'/admin/version/phone',
                   headers={"token":self.initialToken},
                   json=self.list_dumps(content))
        obj=json.loads(r.text)
        assert obj['code'] is None

    def test_uploadApp_common_cooker(self):
        content={
        "version": version_e,
        "force": True,
        "last_force_version": "0.0.1",
        "description": "修改界面布局\n启用蜜饼工坊测试样本"
        }
        r=requests.post(URL+'/admin/version/phone',
                   headers={"token":self.cookerToken},
                   json=self.list_dumps(content))
        obj=json.loads(r.text)
        assert obj['code'] is None

    def test_uploadApp_common_architect(self):
        content={
        "version": version_f,
        "force": True,
        "last_force_version": "0.0.1",
        "description": "修改界面布局\n启用蜜饼工坊测试样本"
        }
        r=requests.post(URL+'/admin/version/phone',
                   headers={"token":self.architectToken},
                   json=self.list_dumps(content))
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],'A0002')

# 重复版本
    def test_uploadApp_repeated_chef(self):
        content={
        "version": "0.0.1",
        "force": True,
        "last_force_version": "0.0.1",
        "description": "修改界面布局\n启用蜜饼工坊测试样本"
        }
        r=requests.post(URL+'/admin/version/phone',
                   headers={"token":self.initialToken},
                   json=self.list_dumps(content))
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],'C000B')

    def test_uploadApp_repeated_cooker(self):
        content={
        "version": "0.0.1",
        "force": True,
        "last_force_version": "0.0.1",
        "description": "修改界面布局\n启用蜜饼工坊测试样本"
        }
        r=requests.post(URL+'/admin/version/phone',
                   headers={"token":self.cookerToken},
                   json=self.list_dumps(content))
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],'C000B')

    def test_uploadApp_repeated_architect(self):
        content={
        "version": "0.0.1",
        "force": True,
        "last_force_version": "0.0.1",
        "description": "修改界面布局\n启用蜜饼工坊测试样本"
        }
        r=requests.post(URL+'/admin/version/phone',
                   headers={"token":self.architectToken},
                   json=self.list_dumps(content))
        obj=json.loads(r.text)
        self.assertEqual(obj['code'],'A0002')

if __name__ == '__main__':
    unittest.main()