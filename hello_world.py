from bottle import route, run, template, debug

@route('/')
def home_page():
    mythings = ['bike','skis','flyrod']
    return template('hello_world', username='Dan', things=mythings)

debug(True)
run(host='localhost', port=8080)
