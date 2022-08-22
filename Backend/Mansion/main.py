import unittest
import requests
import json

URL = 'http://127.0.0.1:8000'

#
# 针对饼学大厦模块的测试
class Mansion_Module(unittest.TestCase) :
    initialUsername="ceobe"
    initialPassword="fdb04988b4e48c4f16952457e86b8d25"
    initialToken="eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwibnVtX3B3ZF9jaGFuZ2UiOjB9.Le2vog19Tq5tPV6h082HX4dZakYiI7eU4huxe0GfRh8"
    # 上传大厦信息
    def test_uploadMansion(self):
        r=requests.post(URL+'/admin/mansion/upload?idBefore=18.6',
                        headers={"token":self.initialToken},
                        json={
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
        }

    ]
})
        obj=json.loads(r.text)
        assert obj['code'] is None

    # 获取大厦信息
    def test_getMansionId(self):
        r=requests.get(URL+'/admin/mansion/getId',
                        headers={"token": self.initialToken})
        obj=json.loads(r.text)
        assert obj['code'] is None

    # 获取最近大厦号
    def test_getMansionInfo(self):
        r=requests.get(URL+'/admin/mansion/getInfo?mansion_id=18.6',
                        headers={"token":self.initialToken})
        obj=json.loads(r.text)
        assert obj['code'] is None

    # 删除整个大厦
    def test_deleteMansion(self):
        r=requests.post(URL+'/admin/mansion/delete?mansion_id=18.6',
                        headers={"token":self.initialToken})
        obj=json.loads(r.text)
        assert obj['code'] is None

if __name__ == '__main__' :
    unittest.main()