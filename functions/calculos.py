import math

def distancia_plano(a, b):
    d = math.sqrt(((a[0] - b[0])**2) + ((a[1] - b[1])**2))
    return d


def colisao_circulo(a, b):
    if distancia_plano(a.posicao, b.posicao) < (a.raio + b.raio):
        return True
    else:
        return False


def calc_forca_gravitacional(a, b):
    G = 0.005   
    forca_g = (G * (a.massa * b.massa)) / (distancia_plano(a.posicao, b.posicao) ** 2)
    return forca_g


def descobrir_angulo(posicao):
    r = math.atan2(posicao[0], posicao[1])
    a = math.degrees(r)
    return a

def dividir_forca(forca, a, b):
    fx = forca * (a[0]-b[0])/distancia_plano(a, b)
    fy = forca * (a[1]-b[1])/distancia_plano(a, b)
    return fx, fy
    