import json
import time

import requests


url = "https://movie.douban.com/j/chart/top_list"

param = {
    "type": 24,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35"
}

# 用于容纳结果
tmp = []

with open("top100.json", "w", encoding="utf-8") as f:
    # 遍历得到前100的榜单
    while param["start"] != 100:
        res = requests.get(url, params=param, headers=dic)
        tmp.extend(res.json())  # 注意,res.json()返回的已经是一个python对象字典
        param["start"] += 20
        res.close()
        time.sleep(1)
    f.write(json.dumps(tmp, ensure_ascii=False))
