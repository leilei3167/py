import base64

s = r"你好 hello"
# 不能直接编码字符串，需要先转换成字节
bt = s.encode("utf-8")

b64bytes = base64.b64encode(bt)
b64str = b64bytes.decode("utf-8")
print(b64str)


# 解码
b = base64.b64decode(b64str).decode("utf-8")
print(b)


print("\n适用于url的base64编解码")

# 避免在url中使用+和/，使用-和_代替
tmp = "abcdefg".encode("utf-8")
b64url = base64.urlsafe_b64encode(tmp)
b64 = base64.b64encode(tmp)
print("url: ", b64url.decode("utf-8"))
print("普通b64: ", b64.decode("utf-8"))
