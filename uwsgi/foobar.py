from bottle import route, response, run, default_app, get, post, request

"""
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
"""

@route('/func', method='POST')
def func_info(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["It works"]
application = default_app()