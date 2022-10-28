import json
import unittest
import requests

URL = 'http://127.0.0.1:8000'

#
class Resource_Module(unittest.TestCase) :
    def test_getResource(self):
        r=requests.get(URL+'/canteen/operate/resource/get')
        obj=json.loads(r.text)
        assert obj['code'] is None

if __name__ == '__main__' :
    unittest.main()