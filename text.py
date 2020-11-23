import requests
from bs4 import BeautifulSoup
import sys

class downloader(object):
    def __init__(self):
        self.names = []
        self.urls = []
        self.nums = [0]

    def get_download_url(self):
        url = "https://www.biquge5200.cc/142_142407/"
        html = requests.get(url=url)
        novel = BeautifulSoup(html.text,features="lxml")
        div = novel.find_all('div',id='list')
        a_prt = BeautifulSoup(str(div),features="lxml")
        a = a_prt.find_all('a')
        self.nums = len(a[15:])
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(each.get('href'))

    def get_contents(self,urls):
        req = requests.get(url=urls)
        html = req.text
        bs = BeautifulSoup(html,features="lxml")
        texts = bsfind_all("div",id='content')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return(texts)

    def writer(self,names,path,texts):
        write_flag = True
        with open('bqg_2.text','a+',encoding='utf-8') as f:
            f.write(names+'\n')
            f.writelines(texts)
            f.write('\n\n')

if __name__=='__main__':
    dl = downloader()
    dl.get_download_url()
    # print(dl.urls)
    print('垃圾小说downloading')
    for i in range(dl.nums):
        dl.writer(dl.names[i], 'bqg_2.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('下载完成')



