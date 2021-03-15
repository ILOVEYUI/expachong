
import requests
import re
import os
import time
import random
ok = 'ok'
url = input('请输入url：')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}
response_1 = requests.get(url=url, headers=headers).text

ex = 'https://e-hentai.org/s/.*?(?="><img)'
topic_t = '(?<="gj">).*?(?=</h1>)'
topic_l = re.findall(topic_t, response_1, re.S)
html_list = re.findall(ex, response_1, re.S)
for topic in topic_l:
    if not os.path.exists(topic):
        os.mkdir(topic)
for list in html_list:
    img_html = requests.get(url=list, headers=headers).text
    exto = '(?<=img" src=")https:.*?.jpg(?=" style)|(?<=img" src=")https:.*?.png(?=" style)'
    img_data = re.findall(exto, img_html, re.S)
    for data in img_data:
        time.sleep(random.random())
        img_down = requests.get(url=data, headers=headers).content
        img_name = data.split('/')[-1]
        imgPath = './' + topic + '/' + img_name
        with open(imgPath, 'wb') as fp:
            fp.write(img_down)
            print("下载成功！！！")
