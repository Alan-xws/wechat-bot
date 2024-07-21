import pyautogui

from 功能 import chartgpt, questongpt


def gpt(chat, msg, content, t):
    if(content == ''):
        chat.SendMsg('主人我在')
        return
    if t % 2 == 1:
        chat.SendMsg('@' + msg.sender_remark + " " + questongpt.gt(content))
    else:
        chat.SendMsg('@' + msg.sender_remark + " " + chartgpt.quary(content))
