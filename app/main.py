import bottle
import os
import random


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    print('index')

    return {
        'name': 'PatStovepipe',
        'color': '#8B3A3A'
    }


@bottle.post('/start')
def start():
    return {
        'name': 'PatStovepipe',
        'color': '#8B3A3A',
        'taunt': 'Pat Stovepipe Starting!'
    }


class Movement:
    # string
    move = ''
    pos = []


@bottle.post('/move')
def move():
    data = bottle.request.json

    moves = []

    snakes = data['snakes']
    curPos = []

    # Find my snake and get current position
    for snake in range(len(snakes)):
        if snake.name == 'PatStovepipe':
            curPos = snake.coords[0]

    x = Movement
    x.move = 'up'
    x.pos = [curPos[0], curPos[1] - 1]
    moves.append(x)
    x.move = 'left'
    x.pos = [curPos[0] - 1, curPos[1]]
    moves.append(x)
    x.move = 'down'
    x.pos = [curPos[0], curPos[1] + 1]
    moves.append(x)
    x.move = 'right'
    x.pos = [curPos[0] + 1, curPos[0]]
    moves.append(x)

    # morerandom = True

    for snake in range(len(snakes)):
        for coord in snake.coords:
            for move in moves:
                if move == coord:
                    moves.remove(move)

    for move in moves:
        if move[0] < 0 or move[0] > 19 or move[1] < 0 or move[1] > 19:
            moves.remove(move)

    rnd = random.randint(0, len(moves) - 1)

    return {
        'move': moves[rnd],
        'taunt': 'Moving'
    }


@bottle.post('/end')
def end():
    # data = bottle.request.json

    return {
        'taunt': 'Pat Stovepipe ending!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8081'))
