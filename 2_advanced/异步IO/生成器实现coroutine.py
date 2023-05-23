def consumer():
    r = ""
    while True:
        # 在执行到yield语句时，consumer函数就停止执行了,执行权交还给调用者,等待调用方下一次调用 send() 方法来恢复执行，而produce函数接着往下执行
        # r是producer通过send发送的值,此处赋值给n,并且将r的值返回给produce函数
        n = yield r
        if not n:
            return
        print("[CONSUMER] Consuming %s..." % n)
        r = "200 OK"


def produce(c):
    # 启动生成器,第一次发送None,会执行到consumer函数的yield语句,并且返回r的值
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("[PRODUCER] Producing %s..." % n)
        # 生产结果发送给consumer函数,并且将consumer函数返回的结果赋值给r
        r = c.send(n)
        print("[PRODUCER] Consumer return: %s" % r)
    c.close()


# 此处不是函数调用，而是一个生成器对象
c = consumer()
# 将生成器对象传入produce函数
produce(c)


# 生成器协程比较麻烦,现在基本不用了,直接使用asyncio模块
