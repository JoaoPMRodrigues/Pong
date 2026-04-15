
def inverte(bola, v, y):
    limite_inferior = 0
    limite_superior = y-bola.height

    if bola.y < limite_inferior:
        bola.y = limite_inferior
    elif bola.y > limite_superior:
        bola.y = limite_superior

    return v*(-1), True


def inverte_sentido(bola, barra, vx, vy, aceleracao, toques):
    vx *= -aceleracao
    if vx > 0:  # Colisão com a barra da esquerda
        bola.x = barra.x + barra.width
    else:  # Colisão com a barra da direita
        bola.x = barra.x - bola.width

    return vx, vy * aceleracao, toques+1
