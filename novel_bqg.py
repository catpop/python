from bs4 import BeautifulSoup
import requests
import sys
class downloader(object):

    def __init__(self):
        self.server = 'https://www.biqukan.com/'
        self.target = 'https://www.biqukan.com/65_65177/'
        self.names = []
        self.urls =[]
        self.nums = 0

    def get_download_url(self):
        req = requests.get(url = self.target)
        web = req.text
        html = BeautifulSoup(web,features="lxml")
        div = html.find_all('div',class_ = "listmain")
        a_bf = BeautifulSoup(str(div),features="lxml")
        a = a_bf.find_all('a')
        self.nums = len(a[15:])
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server +each.get('href'))

    def get_contents(self,target):
        req = requests.get(url = target)
        web = req.text
        html = BeautifulSoup(web)
        texts = html.find_all('div',class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        print(texts)
        return texts

    def writer(self,name,path, text):
        write_flag = True
        with open('bqg.txt','w',encoding='utf-8') as f:
            f.write(name +'\n')
            f.writelines(text)
            f.write('\n\n')
            # print(text)
if __name__=="__main__":
    dl = downloader()
    dl.get_download_url()
    print('垃圾小说downloading')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成')