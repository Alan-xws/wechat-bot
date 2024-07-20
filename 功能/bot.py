import pyautogui

from 功能 import chartgpt, questongpt


def suan(chat, content):
    if len(content) > 4 and content[:4] == '@bot':
        chat.SendMsg(questongpt.gt(content[:4]))
    elif len(content) > 5 and content[:5] == '@chat':
        chat.SendMsg(chartgpt.quary(content[:5]))
    else:
        chat.SendMsg('更多功能还在更新')
