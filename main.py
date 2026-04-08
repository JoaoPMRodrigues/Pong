from pplay.window import *
from pplay.sprite import *
from pplay.collision import *
from pplay.keyboard import *
from rich.traceback import install
install()


def reset_bola(janela, bola):
    bola.x = janela.width//2-bola.width//2
    bola.y = janela.height//2-bola.height//2
    vx = vy = 300
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


def inverte(v):
    return v*(-1), True


def inverte_sentido(vx, vy):
    return vx*-1.05, vy*1.05


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

        if bola.x < 10:
            vx_bola, vy_bola, inicio, vel_b2 = reset(
                janela, bola, barra1, barra2)
            ponto_maquina += 1
        elif bola.x > x - bola.width:
            vx_bola, vy_bola, inicio, vel_b2 = reset(
                janela, bola, barra1, barra2)
            ponto_player += 1

        if bola.y < 0 or bola.y > (y - bola.height):
            vy_bola, mudou = inverte(vy_bola)

        # Colisão

        if Collision.collided(barra1, bola):
            vx_bola, vy_bola = inverte_sentido(vx_bola, vy_bola)
        elif Collision.collided(barra2, bola):
            vx_bola, vy_bola = inverte_sentido(vx_bola, vy_bola)

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
