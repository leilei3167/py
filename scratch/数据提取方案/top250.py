import json
import time
import requests
import re
import csv

url = "https://movie.douban.com/top250"

dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35"
}

# 正则匹配
# 提取名称,评分,年代 ?P<名字> 代表给分组取名字
obj = re.compile(
    r'<li>.*?<div class="item">.*?<em class="">(?P<rank>.*?)</em>.*?'
    r'<span class="title">(?P<name>.*?)'
    r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
    r'<span class="rating_num" property="v:average">(?P<rating>.*?)</span>.*?'
    r"<span>(?P<num>.*?)人评价</span>",
    re.S,
)

# 持久化到文件
l = []
f = open("top250.csv", "w", encoding="utf-8")
csvwriter = csv.writer(f)
f1 = open("top250.json", "w", encoding="utf-8")
jsonRes = []

# 翻页
param = {"start": 0}
for page in range(0, 250, 25):
    param["start"] = page
    res = requests.get(url, params=param, headers=dic)
    content = res.text
    results = obj.finditer(content)

    # 处理正则匹配结果
    for it in results:
        tmp = {
            "rank": it.group("rank"),
            "name": it.group("name"),
            "year": it.group("year").strip(),
            "rating": it.group("rating"),
            "num": it.group("num"),
        }
        csvwriter.writerow(tmp.values())
        jsonRes.append(tmp)
    time.sleep(1)

f1.write(json.dumps(jsonRes, ensure_ascii=False))

print("done")
f.close()
f1.close()
