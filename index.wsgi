def application(environ, start_response):
    body = b'Hello world!\n'
    status = '200OK'
    header=[('Content-type', 'text/plain')]
    start_response(status, headers)
    return[body]
