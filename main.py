from pplay.window import *
from pplay.sprite import *

janela = Window(800, 600)
janela.set_title("[ PONG ]")

bola = Sprite("pong/bolinha.png", 1)
x = janela.width//2-bola.width//2
y = janela.height//2-bola.height//20
velocidade_x = 0.1
velocidade_y = 0.1

barra1 = Sprite("pong/barra.png", 1)
barra2 = Sprite("pong/barra.png", 1)

while True:
    janela.set_background_color((0, 0, 160))

    x += velocidade_x
    y += velocidade_y

    bola.set_position(x, y)
    if x < 0 or x > (800 - bola.width):
        velocidade_x *= -1.05
    if y < 0 or y > (600 - bola.height):
        velocidade_y *= -1

    barra1.set_position(0, 150)
    barra2.set_position(750, 150)

    bola.draw()
    barra1.draw()
    barra2.draw()
    janela.update()
