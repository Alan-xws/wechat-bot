import pyautogui

from 功能 import chartgpt, questongpt


def gpt(chat, msg, who, content, t):
    if (content == ''):
        chat.SendMsg('主人我在')
        return
    if t % 2 == 1:
        if who != msg.sender_remark:
            chat.SendMsg('@' + msg.sender_remark + " " + questongpt.gt(content))
        else:
            chat.SendMsg(questongpt.gt(content))
    else:
        if who != msg.sender_remark:
            chat.SendMsg('@' + msg.sender_remark + " " + chartgpt.quary(content))
        else:
            chat.SendMsg(chartgpt.quary(content))
