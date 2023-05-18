# 将字符串转换为int默认是十进制如果想要其他进制,则需要自己手动指定base
n = "1234"
print(int(n))

n1 = "100101"
print(int(n1, base=2))  # 解析二进制整数


# 如果要解析大量的二进制字节串,每次都设置base参数太麻烦,我们可以基于他创建一个包装函数
def int2(x, base=2):
    return int(x, base)


print(int2("101"))
print(int2("101001"))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
import functools

int3 = functools.partial(int, base=2)
print(int3("101"))
print(int3("1010000"))
print(int3("1010000", base=10))  # 可以覆盖
