"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line

gride = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Draw O player."""
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]



def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    #add condicionais para casa preenchida

    #coluna 1
    if x == -200 and y == 66:
        if (gride[0][0] == 0):
            draw(x, y)
            state['player'] = not player
    
    if x == -200 and y == -67:
        if (gride[1][0] == 0):
            draw(x, y)
            state['player'] = not player

    if x == -200 and y == -200:
        if (gride[2][0] == 0):
            draw(x, y)
            state['player'] = not player

    #coluna 2
    if x == -67 and y == 66:
        if (gride[0][1] == 0):
            draw(x, y)
            state['player'] = not player
    
    if x == -67 and y == -67:
        if (gride[1][1] == 0):
            draw(x, y)
            state['player'] = not player

    if x == -67 and y == -200:
        if (gride[2][1] == 0):
            draw(x, y)
            state['player'] = not player
    
    #coluna 3
    if x == 66 and y == 66:
        if (gride[0][2] == 0):
            draw(x, y)
            state['player'] = not player
    
    if x == 66 and y == -67:
        if (gride[1][2] == 0):
            draw(x, y)
            state['player'] = not player

    if x == 66 and y == -200:
        if (gride[2][2] == 0):
            draw(x, y)
            state['player'] = not player

    update()
    
    # condicionais de preenchimento

    #coluna 1
    if x == -200 and y == 66:
        gride[0][0] = 1
    
    if x == -200 and y == -67:
        gride[1][0] = 1
    
    if x == -200 and y == -200:
        gride[2][0] = 1

    #coluna 2
    if x == -67 and y == 66:
        gride[0][1] = 1
    
    if x == -67 and y == -67:
        gride[1][1] = 1
    
    if x == -67 and y == -200:
        gride[2][1] = 1
    
    #coluna 3
    if x == 66 and y == 66:
        gride[0][2] = 1
    
    if x == 66 and y == -67:
        gride[1][2] = 1
    
    if x == 66 and y == -200:
        gride[2][2] = 1



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
