# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request
import re

pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')

def getImg(site_url: str):
    # 访问网站
    url = requests.get(site_url)
    # 获取网站数据
    html = url.text
    # print(html)
    # 创建对象，解析网页，lmxl
    soup = BeautifulSoup(html, "html.parser")
    # 获取所有img标签
    imgTags = soup.find_all("img")
    print(len(imgTags))
    for imgTag in imgTags:
        # 单张图片
        # imgUrl = imgTag.get("data-vpf-src")

        # 不同尺寸大小的图片
        imgs_set_str = imgTag.get("data-vpf-srcset")
        for imgs_url_and_size_str in imgs_set_str.split(","):
            # https://leaveastory.com/wp-content/uploads/2018/03/359-500x500.png 500w
            img_url = imgs_url_and_size_str.split(" ")[0]
            img_name = pattern.findall(img_url)
            if(img_name):
                urllib.request.urlretrieve(img_url,"./leave_a_story/image/%s.png" % img_name[0])
getImg("https://leaveastory.com/?vp_page=2")
