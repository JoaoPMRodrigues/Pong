from pplay.window import *
from pplay.sprite import *
from pplay.collision import *
from pplay.keyboard import *
from random import randint
from rich.traceback import install
install()


def reset_bola(janela, bola):
    bola.x = janela.width//2-bola.width//2
    bola.y = janela.height//2-bola.height//2
    vx = vy = 300
    while True:
        aleatorio = randint(-1, 1)
        if aleatorio != 0:
            vx *= aleatorio
            break
    while True:
        aleatorio = randint(-1, 1)
        if aleatorio != 0:
            vy *= aleatorio
            break
    return vx, vy, False


def reset_barra(janela, barra):
    barra.y = janela.height//2-barra.height//2
    return 350


def reset(janela, bola, barra1, barra2):
    vxb, vyb, ini = reset_bola(janela, bola)
    vb1 = reset_barra(janela, barra1)  # Velocidade do player desconsidera
    vb2 = reset_barra(janela, barra2)
    return vxb, vyb, ini, vb2


def movimento_bola(bola, vx, vy, dt):
    bola.x += vx*dt
    bola.y += vy*dt


def movimento_player(barra, teclado, dt, y):
    if teclado.key_pressed("UP") and barra.y > 0:
        barra.y -= 300 * dt
    elif teclado.key_pressed("DOWN") and barra.y < (y-barra.height):
        barra.y += 300 * dt


def movimento_ia(barra, mudou, vel, dt, y):
    barra.y += vel*dt
    if mudou or barra.y < 0 or barra.y > (y - barra.height):
        vel *= -1
    return False, vel


def inverte(bola, v, y):
    limite_inferior = 0
    limite_superior = y-bola.height

    if bola.y < limite_inferior:
        bola.y = limite_inferior
    elif bola.y > limite_superior:
        bola.y = limite_superior

    return v*(-1), True


def inverte_sentido(bola, barra, vx, vy, aceleracao):
    vx *= -aceleracao
    if vx > 0:  # Colisão com a barra da esquerda
        bola.x = barra.x + barra.width
    else:  # Colisão com a barra da direita
        bola.x = barra.x - bola.width

    return vx, vy * aceleracao


def placar(janela, texto):
    janela.draw_text(texto, janela.width//2 - 60, 20, cor="white", tamanho=50)


# Define janela
x = 800
y = 600
janela = Window(x, y)
janela.set_title("[ PONG ]")
inicio = False

# Define Bola
bola = Sprite("Sprites/bola.png", 1)
bola.x = janela.width//2-bola.width//2
bola.y = janela.height//2-bola.height//20
vx_bola = 300
vy_bola = 300
aceleracao = 1.01

# Define barra1 (Player)
barra1 = Sprite("Sprites/barra.png", 1)
barra1.x = 5
barra1.y = janela.height//2-barra1.height//2

# Define barra2 (IA)
barra2 = Sprite("Sprites/barra.png", 1)
barra2.x = 780
barra2.y = janela.height//2-barra2.height//2
vel_b2 = 350
mudou = False

# Define placar

ponto_maquina = 0
ponto_player = 0
texto = f"{ponto_player} X {ponto_maquina}"

# Define Teclado
teclado = Keyboard()

while True:
    janela.set_background_color((0, 0, 160))
    if teclado.key_pressed("SPACE"):
        inicio = True

    if inicio:
        dt = janela.delta_time()

        # Movimento da bola
        movimento_bola(bola, vx_bola, vy_bola, dt)

        # Reset após pontução
        if bola.x < 10:
            vx_bola, vy_bola, inicio, vel_b2 = reset(
                janela, bola, barra1, barra2)
            ponto_maquina += 1
        elif bola.x > x - bola.width:
            vx_bola, vy_bola, inicio, vel_b2 = reset(
                janela, bola, barra1, barra2)
            ponto_player += 1

        # Colisão com os limites da tela
        if bola.y < 0 or bola.y > (y - bola.height):
            vy_bola, mudou = inverte(bola, vy_bola, y)

        # Colisão com as barras
        if Collision.collided(barra1, bola):
            vx_bola, vy_bola = inverte_sentido(
                bola, barra1, vx_bola, vy_bola, aceleracao)
        elif Collision.collided(barra2, bola):
            vx_bola, vy_bola = inverte_sentido(
                bola, barra2, vx_bola, vy_bola, aceleracao)

        # Movimento da barra1 (Player)
        movimento_player(barra1, teclado, dt, y)

        # Movimento da Barra 2 (IA)
        mudou, vel_b2 = movimento_ia(barra2, mudou, vel_b2, dt, y)

    # Placar
    placar(janela, f"{ponto_player} X {ponto_maquina}")

    # Desenhho
    bola.draw()
    barra1.draw()
    barra2.draw()
    janela.update()
