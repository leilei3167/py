# 相比于标准库的urllib，requests更加简洁易用,能够非常方便的添加处理请求头，cookie，代理，超时，认证等功能。

# pip install requests 安装requests库

import requests
from urllib.request import urlopen

url = "https://www.sogou.com/web?query=%E5%91%A8%E6%9D%B0%E4%BC%A6"
# 如果不设置headers,将会被大多数网站屏蔽
dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35"
}


response = requests.get(url, headers=dic)

# print(response)
print(response.text)
