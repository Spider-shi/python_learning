#-*-coding:utf-8-*-
#! /usr/bin/env python
# Filename : grabWeb.py

'''
urllib.urlretrieve

urlretrieve(url, filename = None, reporthook = None, data = None)

Parameters:
    filename : 指定了保存本地路径(如果未指定参数，urllib会生成一个临时文件保存数据)

    reporthook: 回调函数，当链接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用\
                            回调函数来显示当前的下载进度

    data: 指post到服务器的数据，该方法返回一个包含两个元素的(filename, headers)元组，filename表示保存到\
                本地的路径，header表示服务器的响应头
'''
from urllib import urlretrieve

def firstNonBlank(lines):
    for eachline in lines:
        if not eachline.strip():
            continue
        else:
            return eachline


def firstLast(webPage):
    f = open(webPage)
    lines = f.readlines()
    f.close()
    print firstNonBlank(lines)
    lines.reverse()
    print firstNonBlank(lines)


def downLoad(url = "http://www.sina.com.cn", process = firstLast):
    try:
        retval = urlretrieve(url, 'sina.html')[0]
    except IOError:
        retval = None

    if retval:
        process(retval)

if __name__ == "__main__":
    downLoad()
