# WSGI 分为两部分,一个是web-server(处理器),另一部分是web-application

import os
import sys

from app import simple_app


def wsgi_to_bytes(s):
    return s.encode()


def run_with_cgi(application):
    environ = dict(os.environ.items())
    environ['wsgi.input'] = sys.stdin.buffer
    environ['wsgi.errors'] = sys.stderr
    environ['wsgi.version'] = (1, 0)
    environ['wsgi.multithread'] = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once'] = True
    if environ.get('HTTPS', 'off') in ('on', '1'):
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'

    headers_set = []
    headers_sent = []

    # 写到标准输出而不是响应http
    def write(data):
        out = sys.stdout.buffer
        if not headers_set:
            raise AssertionError("write()before start_response()")

        elif not headers_sent:
            # 先将headers_set赋值给headers_sent(为副本),并同时将这个副本赋值给status,response_headers
            status, response_headers = headers_sent[:] = headers_set
            out.write(wsgi_to_bytes('Status: %s\r\n' % status))
            for header in response_headers:
                out.write(wsgi_to_bytes('%s: %s \r\n' % header))
            out.write(wsgi_to_bytes('\r\n'))
            out.flush()

    # 定义处理
    def statr_response(status, response_headers, exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    raise (exc_info[0], exc_info[1], exc_info[2])
            finally:
                exc_info = None
        elif headers_set:
            raise AssertionError("Headers already set!")

        headers_set[:] = [status, response_headers]
        # 注意 返回的是write函数
        return write

    # 我们定义的WSGI应用程序(WSGI-application),必须是可调用对象它接收两个参数：一个是包含HTTP请求信息的environ字典，另一个是一个可调用的start_response函数。
    # WSGI应用程序根据传入的请求信息生成HTTP响应内容，并通过调用start_response函数来设置响应头和状态码
    # application必须是一个可调用对象,是一个函数或者是一个有__call__的类的实例
    # 其返回值只需返回一个可迭代对象即可
    result = application(environ, statr_response)

    # 遍历我们处理器函数返回的值,生成最终的处理结果返回客户端
    try:
        for data in result:
            if data:
                write(data)
        if not headers_sent:
            write(' ')
    finally:
        if hasattr(result, 'close'):
            result.close()


if __name__ == '__main__':
    run_with_cgi(simple_app)
# gateway可以视为一种WSGI服务器(实际上他并没有接收http请求,和响应,只是调用了application并将结果打印至终端)

# WSGI服务器负责接收http请求,并将http请求交给WSGI-application处理,并将处理结果生成响应发送回客户端
# WSGI可以独立运行,WSGI可以启动指定的WSGI应用程序
# 除直接运行本文件外,可以通过现有的WSGI服务器启动WSGI application: gunicorn app:simple_app
