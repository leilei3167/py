import re

import requests


url = "https://dy.dytt8.net/index2.htm"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35"
}

obj = re.compile(
    r'最新电影更新:.*?<a\shref=.*?《(?P<name>.*?)[》|<].*?<div class="bd3r">',
    re.S,
)

res = requests.get(url, verify=False, headers=headers)
res.encoding = "gb2312"  # 注意 和网页的编码要一致(head标签里面的charset)
result = obj.finditer(res.text)
for r in result:
    print(r.group("name"))
