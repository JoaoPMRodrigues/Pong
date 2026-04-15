from random import randint


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
    return 300


def reset(janela, bola, barra1, barra2):
    vxb, vyb, ini = reset_bola(janela, bola)
    # Velocidade do player desconsidera
    vb1 = reset_barra(janela, barra1)
    vb2 = reset_barra(janela, barra2)

    return vxb, vyb, ini, vb2,
