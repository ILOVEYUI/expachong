import requests
import re
import os

if not os.path.exists('./ehthree'):
    os.mkdir('./ehthree')
url = 'https://e-hentai.org/g/1867227/c51494ab71/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

response_1 = requests.get(url=url, headers=headers).text
ex = 'https://e-hentai.org/s/.*?(?="><img)'
html_list = re.findall(ex, response_1, re.S)
for list in html_list:
    img_html = requests.get(url=list, headers=headers).text
    exto = '(?<=img" src=")https:.*?.jpg(?=" style)|(?<=img" src=")https:.*?.png(?=" style)'
    img_data = re.findall(exto, img_html, re.S)
    for data in img_data:
        img_down = requests.get(url=data, headers=headers).content
        img_name = data.split('/')[-1]
        imgPath = './ehthree/' + img_name
        with open(imgPath, 'wb') as fp:
            fp.write(img_down)
            print("下载成功！！！")
