import requests
import re
import setting_f
import os
import time
import random


def wenjianjia(topic_l):
    """提取漫画名并创建对应文件夹"""
    for topic in topic_l:
        if not os.path.exists(topic):
            os.mkdir(topic)
        return topic


def qingqiu(url):
    """各种乱七八糟的请求"""

    response_1 = requests.get(url=url, headers=setting_f.headers, verify=False).text  # 请求漫画页面的html
    topic_l = re.findall(setting_f.topic_t, response_1, re.S)  # 请求漫画名（获得的是单元素列表，需要提取）
    topic = wenjianjia(topic_l)  # 提取漫画名并创建对应文件夹
    html_list = re.findall(setting_f.ex, response_1, re.S)  # 获取漫画单页具体页面的url（列表）
    for list in html_list:  # 提取单页漫画url
        img_html = requests.get(url=list, headers=setting_f.headers, verify=False).text  # 获取url对应漫画页html
        img_data = re.findall(setting_f.exto, img_html, re.S)  # 获取图片url（单元素列表）
        for data in img_data:  # 提取图片url
            download(data, topic)


def download(data, topic):
    """下载图片"""
    time.sleep(random.uniform(1, 3))  # 随机休眠1-3秒
    print(data)
    img_down = requests.get(url=data, headers=setting_f.headers, verify=False).content  # 二进制形式下载图片
    img_name = data.split('/')[-1]  # 以图片名最后作为文件名
    imgPath = './' + topic + '/' + img_name  # 图片路径
    # 将图片数据写入文件
    with open(imgPath, 'wb') as fp:
        fp.write(img_down)
        print(img_name + "下载成功！！！")
