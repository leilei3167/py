# 统计每次请求消耗的时间

import re
import time


from django.urls import reverse

# 注意,这是用来兼容老代码的措施,如果是新代码,则直接用新方法编写(自己在__call__方法中处理process_request和process_view)
from django.utils.deprecation import MiddlewareMixin


# 完整的中间件接口示例:
class TimeItMiddleware(MiddlewareMixin):
    # 请求来到中间件中时的第一个方法,一般我们在这做一些简单校验,登录或者判断请求中的http请求头等
    # 可以直接返回HttpResponse或返回None会继续执行后续的方法
    def process_request(self, request):
        self.start_time = time.time()
        return

    # 第二个执行的方法,其中func就是我们要执行的view处理器,返回None就是继续执行后续的处理器
    def process_view(self, request, func, *args, **kwargs):
        # reverse是根据给出的view的name来反向解析出对应的url
        # 此处判断如果不是访问首页,则不统计时间
        if request.path != reverse("index"):
            return None

        start = time.time()
        # 执行业务逻辑,获得response
        response = func(request)
        costed = time.time() - start
        print("process view: {:.2f}s".format(costed))
        return response

    # 在产生异常时就会进入这个方法,如果返回None,则继续执行后续的方法,如果整个阶段没有发生任何异常,则不会执行
    # 此处可以用来记录异常日志
    # 注意,如果在process_view中手动调用了func,则不会触发process_exception
    # 用于做异常的处理,如果不指定逻辑,Django会有自己的异常模板
    def process_exception(self, request, exception):
        pass

    # 如果使用类render()方法来渲染模板,则会先执行process_template_response()方法
    # 一般设置一下Content-Type等
    def process_template_response(self, request, response):
        return response

    # 所有中间件执行完毕后执行的方法,一般用来做一些清理工作,此方法对所有的请求都会执行
    # 而上一个方法只对使用了render()方法的响应执行
    def process_response(self, request, response):
        # time.sleep(1)
        costed = time.time() - self.start_time
        print("request to response cose: {:.2f}s".format(costed))
        return response


# 也可以使用函数式的中间件,其接受get_response参数(view处理器,或者中间件链上的下一个中间件)其可调用并返回中间件
def some_mid(get_response):
    def mid(request):
        print("before")
        response = get_response(request)
        print("after")
        return response

    # 返回的是中间件
    return mid


# 或者写成类,必须实现__call__方法(上述从MiddlewareMixin继承的中间件就是这样实现的)
class SimpleMid:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, resquest):
        print("before")
        response = self.get_response(resquest)
        print("after")
        return response
