import unittest
import requests
import json

URL = 'http://127.0.0.1:8000'

# 针对版本模块的测试
class Version_Module(unittest.TestCase) :
    initialUsername="ceobe"
    initialPassword="fdb04988b4e48c4f16952457e86b8d25"
    initialToken="eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwibnVtX3B3ZF9jaGFuZ2UiOjB9.Le2vog19Tq5tPV6h082HX4dZakYiI7eU4huxe0GfRh8"
    # 上传插件版本
    def test_uploadPlugin(self):
        r=requests.post(URL+'/admin/version/plugin',
                       headers={"token":self.initialToken},
                       json={
	"version": "5.0.0",
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

    # 上传app版本
    def test_uploadApp(self):
        r=requests.post(URL+'/admin/version/phone',
                   headers={"token":self.initialToken},
                   json={
	"version": "0.0.2",
	"force": "true",
	"last_force_version": "0.0.1",
	"description": "修改界面布局\n启用蜜饼工坊测试样本"
})
        obj=json.loads(r.text)
        assert obj['code'] is None

if __name__ == '__main__':
    unittest.main()