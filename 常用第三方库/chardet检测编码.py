import chardet

asc = chardet.detect(b"Hello,world!")
print(asc)

d = "离离原上草，一岁一枯荣".encode("gbk")
print(chardet.detect(d))
