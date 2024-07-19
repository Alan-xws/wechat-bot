import requests
url = "https://fanyi.baidu.com/sug"
def fanyi(s):
    data = {"kw":s}
    resp = requests.post(url,data = data)
    print(resp.json())
    return resp.json()['data']

