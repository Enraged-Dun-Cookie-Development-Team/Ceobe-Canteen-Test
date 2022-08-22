import json
import unittest
import requests

URL = 'http://127.0.0.1:8000'

class Version_Module(unittest.TestCase) :
    def test_getAppVersion(self):
        r=requests.get(URL+'/canteen/operate/announcement/list')
        obj=json.loads(r.text)
        assert obj['code'] is None


if __name__ == '__main__' :
    unittest.main()