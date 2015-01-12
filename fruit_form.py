import bottle

@bottle.route('/')
def home_page():
    mythings = ['skis','bike','flyrod','moto']
    return bottle.template('hello_world',username="Dan Finn", things=mythings)

@bottle.post('/favorite_sport')
def favorite_sport():
    sport = bottle.request.forms.get("sport")
    if (sport == None or sport == ""):
        sport = "No sport selected"

    return bottle.template('fruit_selection.tpl', {'sport':sport})

bottle.debug(True)
bottle.run(host='localhost',port=8080)
