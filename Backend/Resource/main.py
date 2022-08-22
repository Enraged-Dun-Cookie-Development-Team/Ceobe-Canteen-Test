import unittest
import requests
import json

URL = 'http://127.0.0.1:8000'

#
# 针对资源模块的测试
class Resource_Module(unittest.TestCase) :
    initialUsername="ceobe"
    initialPassword="fdb04988b4e48c4f16952457e86b8d25"
    initialToken="eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwibnVtX3B3ZF9jaGFuZ2UiOjB9.Le2vog19Tq5tPV6h082HX4dZakYiI7eU4huxe0GfRh8"
    # 上传资源内容
    def test_uploadResource(self):
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
        obj=json.loads(URL+'/admin/resource/submitList')
        assert obj['code'] is None

    # 获取资源内容
    def test_getResourceList(self):
        r=requests.get(URL+'/admin/resource/list',
                       headers={"token":self.initialToken})
        obj=json.loads(r.text)
        assert obj['code'] is None

if __name__ =='__main__':
    unittest.main()