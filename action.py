from function import getNext,getPage

# page = 153066
# nxtPage = getNext(page)
#
# while nxtPage:
#     curPage = getPage(nxtPage)
#
#
# 153074

# for curPage in range(153066,153074):
#     getPage(curPage)


curPage = 153271

while curPage != 4270109:
    curPage = getPage(curPage)
    nxtPage = getNext(curPage)
    curPage = nxtPage
    if int(curPage) == 4270109:
        break



