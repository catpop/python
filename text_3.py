import requests,sys
from lxml import etree

# class get_downloader(object):
#     def __init__(self):
#         self

#     def get_download_url(self):
#         url = requests.get(url ='99csw.com/book/2744/index.htm')

#         99csw.com/book/2744(+num+)/index.htm

for i in range(1):
    url = "https://www.99csw.com/book/2744/{}.htm".format(83204+i)
    response = requests.get(url=url)
    contents = etree.HTML(response.content)

    html = contents.xpath('//*[@id="content"]/div')
    print(len(html))
    for tmp in html:
        with open ('novel.text','a+',encoding='utf-8') as f:
            print(tmp.text)
            f.writelines(tmp.text)
            f.write('\n')
