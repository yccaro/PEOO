"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *
from freegames import line
import random #importando biblioteca para jogadas aleatórias

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

#add nova cor e espessura 
def drawx(x, y):
    """Draw X player."""
    width(5)
    color('red')
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

#add nova cor e espessura 
def drawo(x, y):
    """Draw O player."""
    up()
    goto(x + 67, y + 5)
    down()
    width(5)
    color('blue')
    circle(62)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200
    #a primeira parte do cauculo identifica em qual casa o jogador teclou
    #já a última parte dimenciona onde a casa fica no tabuleiro

#função para gerar a jogada aleatória
def jogadaAleatoria():
    #cria uma lista para as casas vazias no gride
    casaVazia = []

    for i in range(3): #para cada uma das tres linhas
        for j in range(3): #para cada uma das tres colunhas na linhas
            if gride[i][j] == -1: # se estiver vazio
                casaVazia.append((i, j)) # adiciona na lista das posições vazias

    if casaVazia:
        linha, coluna = random.choice(casaVazia)
        x = linha * 133 - 200 #dimenciona pela posição escolhida onde fica no tabuleiro
        y = coluna * 133 - 200 #dimenciona pela posição escolhida onde fica no tabuleiro
        tap(x, y)

#função para ver se ouve vitória
def checarVitoria(player):
    #para cada uma das tres linhas
    for i in range(3):
        #se todas as posiçoes da linha são do msm jogador ou todas as posiçoes da coluna são do mesmo jogador
        if all(gride[i][j] == player for j in range(3)) or all(gride[j][i] == player for j in range(3)):
            return True

    #se todas as posiçoes da diagonal principal são do msm jogador ou todas as posiçoes da outra diagonal são do mesmo jogador
    if all(gride[i][i] == player for i in range(3)) or all(gride[i][2 - i] == player for i in range(3)):
        return True

    return False

state = {'player': 0}
players = [drawx, drawo]
gride = [[-1, -1, -1], 
         [-1, -1, -1], 
         [-1, -1, -1]]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']

    #identifica em qual casa o jogador teclou no gride
    linha = int((x + 200) // 133) 
    coluna = int((y + 200) // 133)

    if gride[linha][coluna] == -1:
        draw = players[player]
        draw(x, y)
        gride[linha][coluna] = player
        update()

        if checarVitoria(player):
            print(f"Jogador {player + 1} venceu!")

        state['player'] = not player

        if state['player'] == 1:
            jogadaAleatoria()



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
