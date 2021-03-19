import urllib3
from shuru import shuru
import download
urllib3.disable_warnings()  # 去除无必要关心的警告

url = shuru()  # 输入漫画网址
download.qingqiu(url)#各种requests


