
def movimento_bola(bola, vx, vy, dt):
    bola.x += vx*dt
    bola.y += vy*dt


def movimento_player(barra, teclado, dt, y, esp=0):
    if teclado.key_pressed("UP") and barra.y > 0:
        barra.y -= 300 * dt
    elif teclado.key_pressed("DOWN") and barra.y < (y-barra.height-esp):
        barra.y += 300 * dt


def movimento_ia(barra, mudou, vel, dt, y, esp=0):
    barra.y += vel*dt
    if mudou:
        vel *= -1
    elif barra.y < 0:
        barra.y = 0
        vel *= -1
    elif barra.y > (y - barra.height-esp):
        barra.y = y-barra.height-esp
        vel *= -1

    return False, vel
