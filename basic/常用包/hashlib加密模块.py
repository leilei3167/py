# MD5
import hashlib
import time

key = "some_key"


def generate_token():
    a_time = int(time.time())
    _token = "%s%s" % (key, a_time)  # 以密钥和时间戳为基础生成token
    hashobj = hashlib.sha1(_token.encode("utf-8"))  # 生成一个hash对象
    return hashobj.hexdigest(), a_time


def verfiy_token(token, a_time):
    _token = "%s%s" % (key, a_time)  # 用解密出来的时间戳和密钥生成token,对比
    hashobj = hashlib.sha1(_token.encode("utf-8"))
    if hashobj.hexdigest() == token:
        return True
    return False


t1, time_stamp = generate_token()
t2 = "somehdsaihiasd"
if verfiy_token(t2, time_stamp):
    print("ok")
else:
    print("t2 token无效")

if verfiy_token(t1, time_stamp):
    print("t1 ok")
else:
    print("t1 token无效")
