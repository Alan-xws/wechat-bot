import requests
from bs4 import BeautifulSoup
from datetime import datetime


def cut(s):
    l = 0
    r = len(s) - 1
    while s[l] != '>':
        l += 1
    while s[r] != '+':
        r -= 1
    return s[l + 1:r]


def cut1(s):
    l = 0
    r = len(s) - 1
    while s[l] != '>':
        l += 1
    while s[r] != '<':
        r -= 1
    return s[l + 1:r]


def cut2(s):
    l = 0
    r = len(s) - 1
    while s[l] != '"':
        l += 1
    while s[r] != '"':
        r -= 1
    return s[l + 1:r]


def addt(s):
    sl = s.split(' ')
    sll = sl[1].split(':')
    sll[0] = str(int(sll[0]) - 1)
    return f'{sl[0]} {sll[0]}:{sll[1]}:{sll[2]}'


def at(chat, atlen):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    res = requests.get("https://atcoder.jp/contests", headers=headers).text
    # print(res)
    soup = BeautifulSoup(res, "html.parser")
    data = soup.select("td a time")
    addres = soup.select("td a")
    for i in range(len(addres) - 2 * len(data)):
        addres.pop(0)
    for i in range(len(addres) - 2, -1, -2):
        addres.pop(i)
    ans = ''
    for i in range(min(len(data), atlen)):
        d = data[i]
        now = datetime.now()
        if cut(str(d)) + '1:00' > now.strftime('%Y-%m-%d %H:%M:%S'):
            ans += f'{cut1(str(addres[i]))}\n比赛时间 -> {addt(cut(str(d)))[:-3]}\n比赛地址 -> https://atcoder.jp{cut2(str(addres[i]))}\n\n'
    chat.SendMsg(ans)
