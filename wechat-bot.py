import time
import random

# import pyautogui
from wxauto import *

from 功能 import replyfanyi, updatecf, bot, todo
from 功能 import adduser
from 爬虫 import dailyproblem, atcoder

# 打开微信客户端
wx = WeChat()
# cf竞赛
cf = '待更新'
# 输出atcoder长度
atlen = 1
# 用户列表
listen_list = ['bot测试群']
# 加入到监听用户列表
for user in listen_list:
    wx.AddListenChat(who=user, savepic=False)
# 刷新时间
wait = 1
# 关机 code
atcoderlist = []
password = random.randint(1, 1000)
wx.SendMsg('密码' + str(password), 'Alanbeacker')
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
            try:
                if msgtype == 'friend' and content == 'cf':
                    chat.SendMsg(cf)
                # 回复翻译
                # elif msgtype == 'friend' and len(content) >= 2 and content[0:2] == '翻译':
                #     replyfanyi.fanyi(chat, content)
                # 更新cf数据
                elif msgtype == 'friend' and content == 'updatecf' + str(password):
                    cf = updatecf.updatecf(chat)
                # 加入用户监听
                elif msgtype == 'friend' and who == 'Alanbeacker' and len(content) > 3 and content[
                                                                                           :3] == 'add':
                    adduser.add(content, wx, chat)
                # 输出灵茶每日一题
                elif msgtype == 'friend' and content == '每日茶':
                    dailyproblem.get0x3f(chat)
                # 更新 atcoder
                elif msgtype == 'friend' and content == 'updateat' + str(password):
                    atcoderlist = atcoder.at(chat)
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
                # 关机+code
                elif msgtype == 'friend' and len(content) > 2 and content[:2] == '关机' and content == '关机' + str(
                        password):
                    chat.SendMsg('主人再见')
                    exit()
                elif msgtype == 'friend' and len(content) > 7 and content[:7] == 'addtodo':
                    todo.addtodo(str(msg.sender_remark), content[7:])
                    chat.SendMsg('@' + msg.sender_remark + " " + '添加成功')
                elif msgtype == 'friend' and content == 'deltodo':
                    todo.deltodo(str(msg.sender_remark))
                    chat.SendMsg('@' + msg.sender_remark + " " + '清空成功')
                elif msgtype == 'friend' and content == 'outtodo':
                    msgdata = todo.outtodo(str(msg.sender_remark))
                    msgto = '@' + msg.sender_remark + '\n'
                    x = 1
                    for data in msgdata:
                        msgto += str(x) + '.' + data + "\n"
                        x += 1
                    print(msgto)
                    chat.SendMsg(msgto)
                # gpt 回复
                elif msgtype == 'friend' and len(content) > len(str(wx.nickname)) + 1 and content[:len(str(
                        wx.nickname)) + 1] == '@' + str(wx.nickname):
                    if content[17:] == '换个风格':
                        gptf += 1
                        chat.SendMsg('@' + msg.sender_remark + " " + '换好了')
                    else:
                        bot.gpt(chat, msg, content[17:], gptf)
            except:
                chat.SendMsg('主人我出错了')
    time.sleep(wait)
