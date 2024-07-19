import requests
from bs4 import BeautifulSoup


def cut(s):
    l = 0
    r = len(s) - 1
    while s[l] != '>':
        l += 1
    while s[r] != '<':
        r -= 1
    return s[l + 1:r]


def get0x3f(chat):
    url = "https://docs.qq.com/sheet/DWGFoRGVZRmxNaXFz?tab=BB08J2"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }
    resp = requests.get(url, headers=headers)
    contest = resp.text
    soup = BeautifulSoup(contest, "html.parser")
    # 使用 findAll 找到所有 class 为 title 的 span 元素
    date = soup.findAll("span", attrs={"class": "T3"})
    problem = soup.findAll("span", attrs={"class": "T4"})
    chat.SendMsg(cut(str(date[0])) + '\n' + cut(str(problem[0])))
