import re
import urllib.request
import bs4


def getPre(page):
    # page = 153066
    url = 'http://www.37zw.com/0/330/'+ str(page) +'.html'
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    html = resp.read()

    soup = bs4.BeautifulSoup(html,'lxml')
    pages = soup.find_all(class_ = 'bottem1')
    # print(str(pages))

    pre = re.search(r'投推荐票</a> <a href="'+'(.*?)'+'.html">上一章',str(pages))
    # print(pre.group(1))
    return pre.group(1)


def getNext(page):
    # page = 153066
    url = 'http://www.37zw.com/0/330/'+ str(page) +'.html'
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    html = resp.read()
    soup = bs4.BeautifulSoup(html,'lxml')
    pages = soup.find_all(class_ = 'bottem1')
    # print(str(pages))
    nxt = re.search(r'章节列表</a> → <a href="'+'(.*?)'+'.html">下一章',str(pages))
    nxtPage = nxt.group(1)
    # print(nxt.group(1))

    return nxtPage

def getPage(page):
    # page = 153066
    # 拼装URL
    curPage = page
    url = 'http://www.37zw.com/0/330/'+ str(page) +'.html'
    # 获取HTML
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    html = resp.read()
    # bs4解析HTML,获取content
    soup = bs4.BeautifulSoup(html,'lxml')
    title = soup.h1.string
    content = soup.find(id='content')
    contents = re.search(r'<div id="content">'+'(.*?)'+'</div>',str(content))
    # 写入文件
    fo = open('book.txt',mode = 'a',encoding = 'utf-8')
    fo.write(str(title)+'\n')
    book_content = str(contents.group(1)).replace('<br/><br/>','\n')
    fo.write(book_content + '\n' + '\n')
    fo.close()

    return curPage
    # print(title)
    # print(contents.group(1))
    # print(pages)


# getPage()
# getNext(153067)
