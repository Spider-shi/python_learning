#! /usr/bin/env python
#-*-coding:utf-8-*-
'''
urlretrieve() 下载实例 可显示下载进度
'''

import urllib
import os

def schedule(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum : 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100

    print '%.2f%%' % percent

def main():
    url = 'http://www.baidu.com.cn'
    local = os.path.join('E:\\GitHubTmp', 'baidu.html')
    urllib.urlretrieve(url, local, schedule)

if __name__ == '__main__':
    main()
