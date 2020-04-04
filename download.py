#!/usr/bin/env python3
import requests

def download(url):
    '''
    从指定的 URL 中下载文件并存储到当前目录
    url: 要下载页面内容的网址
    '''
    # 检查 URL 是否存在
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    # 检查是否成功访问了该网站
    if req.status_code == 403:
        print('You do not have the authority to access this page.')
        return
    filename = url.split('/')[-1]
    with open(filename, 'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")

if __name__ == '__main__':
    url = input('Enter a URL: ')
    download(url)


'''
你可能已经注意到了 if __name__ == '__main__': 这条语句，
它的作用是，只有在当前模块名为 __main__ 的时候（即作为脚本执行的时候）才会执行此 if 块内的语句。
换句话说，当此文件以模块的形式导入到其它文件中时，if 块内的语句并不会执行。

你可以将上面的程序修改的更友好些。举个例子，你可以检查当前目录是否已存在相同的文件名。
os.path 模块可以帮助你完成这个。
'''
