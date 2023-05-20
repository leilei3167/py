import re
import requests

# 匹配所有结果,返回list,不常用
l = re.findall(r"\d+", "我10086,他1000")
print(type(l), l)


# finditer: 用的最多,返回的是迭代器,将返回一系列match对象,内容需要调用group方法拿到结果
i = re.finditer(r"\d+", "我10086,他1000")
print(type(i), i)
for i1 in i:
    print(i1.group())

# search 返回的就是迭代器中的元素即match对象,search只会检索到一个就返回
s = re.search(r"\d+", "我10086,他1000")
if s != None:
    print(s, s.group())


# # match从头开始匹配,用的不多,相当于在正则加了个^
# m = re.match(r"\d+", "我10086,他1000")
# print(m, m.group())

# 预加载正则表达式,对于复杂正则,避免反复加载

obj = re.compile(r'<a[^>]*\s+href="([^"]*)"[^>]*>(.*?)</a>', re.S)  # re.S让.能匹配换行符


url = "https://movie.douban.com"

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

res = requests.get(url, params=param, headers=dic)
it = obj.finditer(res.text)
for it1 in it:
    # 在group方法中填写对应的捕获组号即可获得捕获组的数据
    print(it1.group(2), ":", it1.group(1))


res.close()
