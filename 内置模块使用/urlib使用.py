from urllib import request

print("发起GET请求:")

with request.urlopen("https://www.baidu.com") as f:
    data = f.read()
    print("Status:", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s: %s" % (k, v))
    print("Data:", data.decode("utf-8"))


print("发起POST请求,需要将参数转换为bytes,并且指定编码格式:")
