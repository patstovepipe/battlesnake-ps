import bottle
import os
import random


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'name': 'PatStovepipe',
        'color': '#00ff00',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json
    head_url = 'http://i.imgur.com/tWoo7jR.png' 

    # TODO: Do things with data

    return {
        'name': 'PatStovepipe',
        'color': '#00ff00',
        'head': head_url,
        'taunt': 'Pat Stovepipe Starting!'
    }


prevmov = ''

@bottle.post('/move')
def move():
    data = bottle.request.json

    move = ''

    prevmov = move 

    while prevmov == move:

        rnd = random.randint(1,4)

        if rnd == 1:
            move = 'up'
            taunt = 'Pat Stovepipe moving up!'
        elif rnd == 2:
            move = 'left'
            taunt = 'Pat Stovepipe moving left!'
        elif rnd == 3:
            move = 'down'
            taunt = 'Pat Stovepipe moving down!'
        elif  rnd == 4:
            move = 'right'
            taunt = 'Pat Stovepipe moving right!'

    # TODO: Do things with data

    return {
        'move': move,
        'taunt': taunt
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'Pat Stovepipe ending!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
