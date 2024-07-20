import pyautogui

from 功能 import chartgpt, questongpt


def gpt(chat,msg,content):
    chat.SendMsg('@'+msg.sender_remark+" "+questongpt.gt(content))
    # chat.SendMsg(chartgpt.quary(content))
