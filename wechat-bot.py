import time
import random

import pyautogui
from wxauto import *

from 功能 import replyfanyi, updatecf, bot
from 功能 import adduser
from 爬虫 import dailyproblem, atcoder

# 打开微信客户端
wx = WeChat()
pyautogui.hotkey('win', 'down')
# cf竞赛
cf = '待更新'
# 输出atcoder长度
atlen = 1
# 用户列表
listen_list = ['Alanbeacker', 'gxt', 'bot测试群', 'ACM算法竞赛群（23届）']
# 加入到监听用户列表
for user in listen_list:
    wx.AddListenChat(who=user, savepic=False)
# 刷新时间
wait = 1
# 关机 code
atcoderlist = []
password = random.randint(1, 1000)
wx.SendMsg('密码' + str(password), 'Alanbeacker')
pyautogui.hotkey('win', 'down')
gptf = 1
while True:
    # 打开监听页面
    msgs = wx.GetListenMessage()
    for chat in msgs:
        who = chat.who
        one_msgs = msgs.get(chat)
        for msg in one_msgs:
            msgtype = msg.type
            content = msg.content
            print(f'【{who}】：{content}')
            # 回复cf
            if msgtype == 'friend' and content == 'cf':
                chat.SendMsg(cf)
                pyautogui.hotkey('win', 'down')
            # 回复翻译
            # elif msgtype == 'friend' and len(content) >= 2 and content[0:2] == '翻译':
            #     replyfanyi.fanyi(chat, content)
            #     pyautogui.hotkey('win', 'down')
            # 更新cf数据
            elif msgtype == 'friend' and content == 'updatecf' + str(password):
                cf = updatecf.updatecf(chat)
                pyautogui.hotkey('win', 'down')
            # 加入用户监听
            elif msgtype == 'friend' and who == 'Alanbeacker' and len(content) > 3 and content[
                                                                                       :3] == 'add':
                adduser.add(content, wx, chat)
                pyautogui.hotkey('win', 'down')
            # 输出灵茶每日一题
            elif msgtype == 'friend' and content == '每日茶':
                dailyproblem.get0x3f(chat)
                pyautogui.hotkey('win', 'down')
            # 更新 atcoder
            elif msgtype == 'friend' and content == 'updateat' + str(password):
                atcoderlist = atcoder.at(chat)

                pyautogui.hotkey('win', 'down')
            elif msgtype == 'friend' and len(content) >= 7 and content[:7] == 'atcoder':
                try:
                    sl = content.split(" ")
                    atlen = eval(sl[1])
                except:
                    atlen = 1
                ans = ''
                for i in range(min(atlen, len(atcoderlist))):
                    ans += atcoderlist[i]
                if ans == '': ans = '待更新'
                chat.SendMsg(ans)
                pyautogui.hotkey('win', 'down')
            # 关机+code
            elif msgtype == 'friend' and len(content) > 2 and content[:2] == '关机' and content == '关机' + str(
                    password):
                chat.SendMsg('主人再见')
                pyautogui.hotkey('win', 'down')
                exit()
            # gpt 回复
            elif msgtype == 'friend' and len(content) > 16 and content[:16] == '@Alanbeacker-Bot':
                if content[17:] == '换个风格':
                    gptf += 1
                    chat.SendMsg('@' + msg.sender_remark + " " + '换好了')
                else:
                    bot.gpt(chat, msg, content[17:], gptf)
                pyautogui.hotkey('win', 'down')
