import time
import pyautogui
from wxauto import *

from 功能 import replyfanyi, updatecf
from 功能 import adduser
from 功能 import suanshu
from 爬虫 import baidufanyi, codeforces, dailyproblem

# 打开微信客户端
wx = WeChat()
pyautogui.hotkey('win', 'down')
# 爬虫实现爬取https://codeforces.com/contests页面待完善
# cf='Codeforces Round 960 (Div. 2)\n' \
#     '开始时间 -> 2024-07-20 22:35\n' \
#     '比赛时长 -> 02:00\n' \
#     '比赛地址 -> https://codeforces.com/contests/1990'\
cflist = codeforces.get_cf_const()
cf = cflist[0] + '\n开始时间 -> ' + cflist[1] + '\n比赛地址 -> ' + cflist[2] + '\n'
# 用户列表
listen_list = ['Alanbeacker', 'gxt', 'ACM算法竞赛群（23届）', 'bot测试群','wxl','yzh']
# 加入到监听用户列表
for user in listen_list:
    wx.AddListenChat(who=user, savepic=False)
# 刷新时间
wait = 1
while True:
    # 打开监听页面
    msgs = wx.GetListenMessage()
    for chat in msgs:
        who = chat.who
        one_msgs = msgs.get(chat)
        for msg in one_msgs:
            msgtype = msg.type
            content = msg.content
            if(content[0]!='#'):
                continue
            content=content[1:]
            print(f'【{who}】：{content}')
            # 回复cf
            if msgtype == 'friend' and content == 'cf':
                chat.SendMsg(cf)
                pyautogui.hotkey('win', 'down')
            # 回复翻译
            elif msgtype == 'friend' and len(content) >= 2 and content[0:2] == '翻译':
                replyfanyi.fanyi(chat, content)
                pyautogui.hotkey('win', 'down')
            # 更新cf数据
            elif msgtype == 'friend' and (who == 'Alanbeacker' or who == 'gxt') and content == 'updatecf':
                updatecf.updatecf(chat)
                pyautogui.hotkey('win', 'down')
            # 加入用户监听
            elif msgtype == 'friend' and (who == 'Alanbeacker' or who == 'gxt') and 'add' in content:
                adduser.add(content, wx)
                pyautogui.hotkey('win', 'down')
            # 输出灵茶每日一题
            elif msgtype == 'friend' and content == '每日茶':
                dailyproblem.get0x3f(chat)
                pyautogui.hotkey('win', 'down')
            elif msgtype == 'friend':
                suanshu.suan(chat, content)
                pyautogui.hotkey('win', 'down')
    time.sleep(wait)
