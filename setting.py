#需要的请求头
headers = {
    'User-Agent': '',
    'Accept-Encoding': 'gzip',
    'Cookie': ''
}
ex = 'https://exhentai.org/s/.*?(?="><img)'#对漫画页面中单页漫画的url正则匹配式
topic_t = '(?<="gj">).*?(?=</h1>)'#匹配漫画名
exto = '(?<=img" src=")https:.*?.jpg(?=" style)|(?<=img" src=")https:.*?.png(?=" style)'  # 图片url正则匹配式