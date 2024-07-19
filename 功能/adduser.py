def add(content, wx):
    useradd = content.split(' ')
    if len(useradd) < 2: return
    adu = useradd[1]
    try:
        wx.AddListenChat(who=adu, savepic=False)
    except LookupError as e:
        print(e)
