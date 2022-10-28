import requests
import json
import hashlib
from Test_case.Common.config_parse import config_parse

URL = config_parse()['URL']

def login_getToken(username, password) :
    loginr = requests.post(URL + '/api/v1/admin/user/login',
                           json={"username" : username,
                                 "password" : password})
    obj = json.loads(loginr.text)
    if (obj['code'] == None) :
        print("login successfully")
        return obj['data']['token']
    else :
        print('login failed error Code:' + obj['code'])

#md5 加密
def exchange_to_md5(content) :
    # 创建md5对象
    md_obj = hashlib.md5()
    # 传入信息进行加密，注意传入的信息必须进行encode编码，否则报错
    md_obj.update(content.encode("utf-8"))
    # 获取加密后的信息
    md_res = md_obj.hexdigest()
    return md_res

def login_check(username,password):
    r = requests.post(URL + '/api/v1/admin/user/create?permission=cooker',
                      headers={"token" : login_getToken(username, exchange_to_md5(password))})
    obj = json.loads(r.text)
    return obj