
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
