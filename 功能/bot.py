import pyautogui

from 功能 import chartgpt, questongpt


def gpt(chat, msg, content, t):
    if t % 2:
        chat.SendMsg('@' + msg.sender_remark + " " + questongpt.gt(content))
    else:
        chat.SendMsg('@' + msg.sender_remark + " " + chartgpt.quary(content))
