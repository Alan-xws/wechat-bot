import pyautogui

wanshan = '功能未完善'
def suan(chat, content):
    try:
        ans = eval(content)
        chat.SendMsg(ans)
        return
    except ZeroDivisionError as e:
        chat.SendMsg(wanshan)
    except SyntaxError as e:
        chat.SendMsg(wanshan)
    except NameError as e:
        chat.SendMsg(wanshan)
