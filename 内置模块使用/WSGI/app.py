# environ包含所有http请求信息的dict对象,start_response是一个发送http响应的函数
def simple_app(environ, start_response):
    print(environ)
    print(start_response)
    status = "200 OK"
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello!!!!\n']
