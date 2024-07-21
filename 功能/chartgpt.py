import requests
import json

def quary(s):
    try:
        msg = s
        sess = requests.get('https://open.drea.cc/bbsapi/chat/get?keyWord=' + msg + '&userName=type%3Dbbs')
        js = sess.text
        js = json.loads(js)
        return js['data']['reply']
    except:
        return "不好意思主人我出错了"
