import unittest
import requests
import json

URL = 'http://127.0.0.1:8000'

# 针对视频模块的测试
class Video_Module(unittest.TestCase) :
    initialUsername="ceobe"
    initialPassword="fdb04988b4e48c4f16952457e86b8d25"
    initialToken="eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwibnVtX3B3ZF9jaGFuZ2UiOjB9.Le2vog19Tq5tPV6h082HX4dZakYiI7eU4huxe0GfRh8"
    # 获得视频详细信息
    def test_getVideoDetail(self):
        r=requests.get(URL + '/admin/video/detail?bv_number=BV1MT411g7Zu',
                       headers={"token": self.initialToken})
        obj=json.loads(r.text)
        assert obj['code'] is None
    # 获取现有视频信息
    def test_getVideoList(self):
        r=requests.get(URL+ '/admin/video/list',
                       headers={"token": self.initialToken})
        obj=json.loads(r.text)
        assert obj['code'] is None

    # 上传视频信息
    def test_submitVideoList(self):
        r=requests.post(URL + '/admin/video/submitList',
                        headers={"token":self.initialToken},
                        json=[
	{
		"bv": "BV19b4y1v7Wa",
		"start_time": "2021-12-24 04:00:00",
		"over_time": "2022-01-04 15:59:59",
		"title": "2022明日方舟新春会「流光启明」庆 典宣传PV",
		"author": "杨颜同学",
		"video_link": "https://www.bilibili.com/video/bv19b4y1v7Wa",
		"cover_img": "http://i0.hdslb.com/bfs/archive/9315a9911f8af1441854a16c93339926b9c66a8b.jpg@@200w_125h_1c.webp"
	},
	{
		"bv": "BV1r3411a7Kg",
		"start_time": "2022-01-20 04:00:00",
		"over_time": "2022-01-24 15:59:59",
		"title": "【手书/四木攰】 旅途",
		"author": "四木攰",
		"video_link": "https://www.bilibili.com/video/bv1r3411a7Kg",
		"cover_img": "https://i1.hdslb.com/bfs/archive/44d3ab354c59f9549f20925e99ddeb55793e8eef.jpg@200w_125h.webp"
	}
])
        obj=json.loads(r.text)
        assert obj['code'] is None

if __name__=='__main__':
    unittest.main()
