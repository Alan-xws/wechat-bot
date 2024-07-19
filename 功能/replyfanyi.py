from 爬虫 import baidufanyi
def fanyi(chat,content):
    s = content[2:]
    if s == '':
        chat.SendMsg('没有这个单词')
    else:
        list = baidufanyi.fanyi(s)
        listmsg = ''
        for data in list:
            listmsg += data['k'] + '\n'
            listmsg += data['v'] + '\n'
        if listmsg != '':
            chat.SendMsg(listmsg)
        else:
            chat.SendMsg('没有这个单词')