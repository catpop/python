# -*- coding: utf-8 -*-
from lxml import etree
import requests

url = "https://www.baidu.com/"

html = requests.get(url).content.decode()
filter = "//*[@id='su']/@value"
html = etree.HTML(html)
res = html.xpath(filter)
print(res[0])


class restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("restaurant_name is {} cuisine_type is {}".format(self.restaurant_name,self.cuisine_type))
    def open_restaurant(self):
        print("fandian kaile ")
        # return'111'
res = restaurant("qwe","asd")
print(res.open_restaurant())
print(res.describe_restaurant())

.*?data-src="(.*?)".*?name.*?a'+'.*?>(.*?)</a>.*?star.*>(.*?)</p>.*?releasetime.*?>(.*?)</p>'
        +'.*?integer"">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'

