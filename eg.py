import requests
from lxml import etree
import re

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
url = 'http://cindythecute.blog.fc2.com/blog-entry-521.html'
proxies = {

    "http":"http://127.0.0.1:1080",
}

def get_novel():
    req = requests.get(url,headers=header,proxies=proxies)
    html = etree.HTML(req.text)
    res = ''
    for i in range(1,10000):
        try:
            novel = html.xpath('//*[@id="main"]/div[1]/div[1]/text()[{}]'.format(i))
            print(novel[0])
            res+=novel[0]+"\n"
        except Exception as e:
            print(e)
            break
    return res


with open('1943.txt','w',encoding='utf-8') as txt:
    txt.write(get_novel())
# //*[@id="main"]/div[1]/div[1]/text()[9]
# //*[@id="main"]/div[1]/div[1]/text()[10]
