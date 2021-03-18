import requests
import re
import os
import time
import random
import urllib3
urllib3.disable_warnings()

url = input('请输入url：')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Encoding': 'gzip',
    'Cookie': 'ipb_member_id=5278247; ipb_pass_hash=096856a5680f63c865bb07fe1a77fdfe; igneous=caa3b6e42;'
}
response_1 = requests.get(url=url, headers=headers, proxies={"https://": '47.89.41.164:80'},verify=False).text

ex = 'https://exhentai.org/s/.*?(?="><img)'
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
        time.sleep(random.uniform(1,3))
        img_down = requests.get(url=data, headers=headers, proxies={"https://": '47.89.41.164:80'},verify=False).content
        img_name = data.split('/')[-1]
        imgPath = './' + topic + '/' + img_name
        with open(imgPath, 'wb') as fp:
            fp.write(img_down)
            print(img_name+"下载成功！！！")