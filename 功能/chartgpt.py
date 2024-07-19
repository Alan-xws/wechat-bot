import requests
import json

def quary(s):
    msg = s
    sess = requests.get('https://open.drea.cc/bbsapi/chat/get?keyWord=' + msg + '&userName=type%3Dbbs')
    js = sess.text
    js = json.loads(js)
    return js['data']['reply']
