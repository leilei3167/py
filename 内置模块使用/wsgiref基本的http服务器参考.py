from wsgiref.simple_server import make_server


# Web Server Gateway Interface  WSGI接口定义非常简单,它只要求Web开发者实现一个函数,就可以响应HTTP请求
# environ包含所有http请求信息的dict对象,start_response是一个发送http响应的函数
def app(environ, start_response):
    print("method: ", environ["REQUEST_METHOD"])
    print("path: ", environ["PATH_INFO"])
    start_response("200 OK", [("Content-Type", "text/html")])
    body = "<h1>Hello, %s!</h1>" % (environ["PATH_INFO"][1:] or "web")
    return [body.encode("utf-8")]


# 如果要调用处理器函数,必须由WSGI服务器来调用,服务器需要从environ中取出HTTP请求信息,然后把HTTP响应的Header和Body发送给浏览器
# python内置了一个WSGI服务器,这个模块叫wsgiref,它是用纯Python编写的WSGI服务器的参考实现


if __name__ == "__main__":
    httpd = make_server("", 8000, app)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
