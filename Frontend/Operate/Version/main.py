import json
import unittest
import requests

URL = 'http://127.0.0.1:8000'

class Version_Module(unittest.TestCase) :
    def test_getAppVersion(self):
        r=requests.get(URL+'/canteen/operate/version/app?version=0.0.1')
        obj=json.loads(r.text)
        assert obj['code'] is None

    def test_getPluginVersion(self):
        r=requests.get(URL+'/canteen/operate/version/plugin?version=3.0.14')
        obj=json.loads(r.text)
        assert obj['code'] is None

if __name__ == '__main__' :
    unittest.main()