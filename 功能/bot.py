import pyautogui

from 功能 import chartgpt, questongpt


def gpt(chat, content):
    chat.SendMsg(questongpt.gt(content))
    # chat.SendMsg(chartgpt.quary(content))
