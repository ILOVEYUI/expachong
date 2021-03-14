#exloli爬取程序的初涉

import requests

#输入信息
kw=input("请输入要搜索的tag：")
url = 'https://e-hentai.org/'
#UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
#搜索参数
for page in range(1,6):
    page=str(page)
    param = {
        'f_cats':'1017',
        'f_search': kw,
        'page':page,
    }

    #获取数据
    response = requests.get(url=url, params=param, headers=headers)

    page_text=response.text
    filename=kw+page+'.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)

print(filename+"保存成功")