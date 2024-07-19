import pyautogui

from 功能 import chartgpt


def suan(chat, content):
    try:
        ans = eval(content)
        chat.SendMsg(content + '=' + ans)
        return
    except ZeroDivisionError as e:
        chat.SendMsg(chartgpt.quary(content))
    except SyntaxError as e:
        chat.SendMsg(chartgpt.quary(content))
    except NameError as e:
        chat.SendMsg(chartgpt.quary(content))
