from 爬虫 import codeforces


def updatecf(chat):
    cflist = codeforces.get_cf_const()
    cf = cflist[0] + '\n开始时间 -> ' + cflist[1] + '\n比赛地址 -> ' + cflist[2] + '\n'
    chat.SendMsg('更新成功')
    return cf
