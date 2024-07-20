def add(content, wx, chat):
    useradd = content.split(' ')
    if len(useradd) < 2: return
    adu = useradd[1]
    try:
        wx.AddListenChat(who=adu, savepic=False)
        chat.SendMsg('加入成功')
    except LookupError as e:
        print(e)
