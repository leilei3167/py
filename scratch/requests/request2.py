import requests

url = "https://fanyi.baidu.com/sug"

s = input("请输入要翻译的:")

dat = {"kw": s}

res = requests.post(url, data=dat)

t = res.json()
print(type(t))
print(t)
