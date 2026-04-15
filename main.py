from pplay.window import *
from pplay.sprite import *
from pplay.collision import *
from pplay.keyboard import *
from lib.reset import reset
from lib.movimento import movimento_bola, movimento_player, movimento_ia
from lib.inverte import inverte, inverte_sentido
from lib.placar import placar
from rich.traceback import install
install()

# Define tela
x = 800
y = 600
janela = Window(x, y)
janela.set_title("[ PONG ]")

# Define caracteristicas do jogo
inicio = False
dividido = False
toques = 0

# define bola
bola = Sprite("Sprites/bola.png")
bola.x = janela.width // 2 - bola.width // 2
bola.y = janela.height // 2 - bola.height // 2
vx_bola = 300
vy_bola = 300
aceleracao = 1.03

# Define barra 1 (Player)
barra1 = Sprite("Sprites/barra.png")
barra1.x = 5
barra1.y = janela.height // 2 - barra1.height // 2

# Define barra 1 separada (Player)
barra1c = Sprite("Sprites/barra_toques.png")
barra1b = Sprite("Sprites/barra_toques.png")
espacamento = bola.height + 40

# Define barra 2 (IA)
barra2 = Sprite("Sprites/barra.png")
barra2.x = x - barra2.width - 5
barra2.y = janela.height // 2 - barra2.height // 2
vel_b2 = 300
mudou = False

# Define barra 3 separada (IA)
barra2c = Sprite("Sprites/barra_toques.png")
barra2b = Sprite("Sprites/barra_toques.png")

ponto_player = ponto_maquina = 0

# Define teclado
teclado = Keyboard()

while True:
    janela.set_background_color((0, 0, 160))
    dt = janela.delta_time()

    if teclado.key_pressed("SPACE"):
        inicio = True

    if toques >= 3 and not dividido:
        dividido = True
        barra1c.x = barra1.x
        barra1c.y = barra1.y
        barra1b.x = barra1.x
        barra1b.y = barra1.y + barra1c.height + espacamento
        barra2c.x = barra2.x
        barra2c.y = barra2.y
        barra2b.x = barra2.x
        barra2b.y = barra2.y + barra2c.height + espacamento

    if inicio:

        movimento_bola(bola, vx_bola, vy_bola, dt)

        if bola.x < 10:
            ponto_maquina += 1
            vx_bola, vy_bola, inicio, vel_b2 = reset(
                janela, bola,
                barra1c if dividido else barra1,
                barra2c if dividido else barra2
            )
            dividido = False
            toques = 0

        elif bola.x > x - bola.width:
            ponto_player += 1
            vx_bola, vy_bola, inicio, vel_b2 = reset(
                janela, bola,
                barra1c if dividido else barra1,
                barra2c if dividido else barra2
            )
            dividido = False
            toques = 0

        if bola.y < 0 or bola.y > (y - bola.height):
            vy_bola, mudou = inverte(bola, vy_bola, y)

        if not dividido:
            if Collision.collided(barra1, bola):
                vx_bola, vy_bola, toques = inverte_sentido(
                    bola, barra1, vx_bola, vy_bola, aceleracao, toques
                )

            elif Collision.collided(barra2, bola):
                vx_bola, vy_bola, toques = inverte_sentido(
                    bola, barra2, vx_bola, vy_bola, aceleracao, toques
                )

        else:
            if Collision.collided(barra1c, bola):
                vx_bola, vy_bola, toques = inverte_sentido(
                    bola, barra1c, vx_bola, vy_bola, aceleracao, toques
                )

            elif Collision.collided(barra1b, bola):
                vx_bola, vy_bola, toques = inverte_sentido(
                    bola, barra1b, vx_bola, vy_bola, aceleracao, toques
                )

            elif Collision.collided(barra2c, bola):
                vx_bola, vy_bola, toques = inverte_sentido(
                    bola, barra2c, vx_bola, vy_bola, aceleracao, toques
                )

            elif Collision.collided(barra2b, bola):
                vx_bola, vy_bola, toques = inverte_sentido(
                    bola, barra2b, vx_bola, vy_bola, aceleracao, toques
                )

        if not dividido:
            movimento_player(barra1, teclado, dt, y)
            mudou, vel_b2 = movimento_ia(barra2, mudou, vel_b2, dt, y)

        else:
            movimento_player(barra1c, teclado, dt, y,
                             barra1c.height + espacamento)
            barra1b.y = barra1c.y + barra1c.height + espacamento
            mudou, vel_b2 = movimento_ia(
                barra2c, mudou, vel_b2, dt, y, barra1c.height + espacamento)
            barra2b.y = barra2c.y + barra2c.height + espacamento

        if not dividido:
            barra1.draw()
            barra2.draw()

        else:
            barra1c.draw()
            barra1b.draw()
            barra2c.draw()
            barra2b.draw()

    else:
        barra1.draw()
        barra2.draw()

    bola.draw()
    placar(janela, f"{ponto_player} X {ponto_maquina}")
    janela.update()
