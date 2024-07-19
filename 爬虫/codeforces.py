import requests
from bs4 import BeautifulSoup


def change_time(times):
    mlist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    timelist = times.split(' ')
    datelist = timelist[0].split('/')
    # print(datelist[0], datelist[1], datelist[2])
    # print(mlist.index(datelist[0]) + 1)
    ans = f'{datelist[2]}-{str(mlist.index(datelist[0]) + 1)}-{datelist[1]} {timelist[1]}'
    return ans


def get_cf_const():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    res = requests.get("https://codeforces.com/contests", headers=headers).text
    # print(res)
    # 把内容丢给 BeautifulSoup 解析
    soup = BeautifulSoup(res, "html.parser")
    # 使用 findAll 找到所有 class 为 title 的 span 元素
    time_films = soup.findAll("span", attrs={"class": "format-time"})
    const_films = soup.findAll("div", attrs={"style": "text-align:center;"})
    # print(time_films)
    test = const_films[0]
    name = ""
    time = time_films[0].string
    id = 0
    for ch in test:
        p = ch.string
        t = "Div"
        ts = str(p)
        if t in ts:
            name = ts
            for j in range(1880, 5000):
                if str(j) in str(ch):
                    id = j
                    break

    lst = time.split(" ")
    h = int(lst[1].split(":")[0]) + 5
    netime = lst[0] + " " + str(h) + ":" + lst[1].split(":")[1]
    url = "https://codeforces.com/contests/" + str(id)
    return name, change_time(netime), url