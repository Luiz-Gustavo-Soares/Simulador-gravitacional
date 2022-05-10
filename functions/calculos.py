import math

def distancia_plano(ponto1, ponto2):
    '''
    -> Calcula a distancia de dois pontos no plano.
    :param ponto1: resebem a posição (x, y) do primeiro ponto
    :param ponto2: resebem a posição (x, y) do primeiro ponto
    :return: distancia
    '''
    d = math.sqrt(((ponto1[0] - ponto2[0])**2) + ((ponto1[1] - ponto2[1])**2))
    return d


def colisao_circulo(circulo1=object, circulo2=object):
    '''
    -> Calcula se dois circulos colidiram.
    :param circulo1: objeto do primeiro circulo.
    :param circulo2: objeto do segundo circulo.
    :return: True se colidiram e False se não.
    '''
    if distancia_plano(circulo1.posicao, circulo2.posicao) < (circulo1.raio + circulo2.raio):
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
    