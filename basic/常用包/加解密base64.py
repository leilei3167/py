import base64


# 将数据编码为base64
def encode(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    elif isinstance(data, bytes):
        data = data
    else:
        raise TypeError("data must be str or bytes")

    # return base64.encodebytes(data).decode("utf-8")  # 每76个字符插入一个换行符
    return base64.b64encode(data).decode("utf-8")  # 不会插入换行符


print(encode("hello world"))
