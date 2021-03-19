#需要的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Encoding': 'gzip',
    'Cookie': 'ipb_member_id=5278247; ipb_pass_hash=096856a5680f63c865bb07fe1a77fdfe; igneous=caa3b6e42;'
}
ex = 'https://exhentai.org/s/.*?(?="><img)'#对漫画页面中单页漫画的url正则匹配式
topic_t = '(?<="gj">).*?(?=</h1>)'#匹配漫画名
exto = '(?<=img" src=")https:.*?.jpg(?=" style)|(?<=img" src=")https:.*?.png(?=" style)'  # 图片url正则匹配式