import pygame
from pygame.locals import *

from corpos import Bola
from uteis import *

pygame.init()

ALTURA = 600
LARGURA = 1000
tela = pygame.display.set_mode((LARGURA, ALTURA))

b = Bola((50, 50), 6)
terra = Bola((LARGURA/2, ALTURA/2), 50, (0,0,255), 1000000)


clock = pygame.time.Clock()
while True:
    clock.tick(50)
    tela.fill((0,0,0))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()

    if pygame.mouse.get_pressed()[0]:
        b.posicao = pygame.mouse.get_pos()
        b.velocidade_x = 5
        b.velocidade_y = 0


    if colisao_circulo(b, terra):
        b.aceleração_x = b.aceleração_y = 0
        b.velocidade_x = b.velocidade_y = 0
        pass
    
    else:
        forca_g = calc_forca_gravitacional(b, terra)
        fx, fy = dividir_forca(forca_g, b.posicao, terra.posicao)
        
        b.aceleração_x = fx/b.massa * -1
        b.aceleração_y = fy/b.massa * -1

        informaçoes = f'''
        Força G = {forca_g}
            Fx = {fx}
            Fy = {fy}

        Aceleração x = {b.aceleração_x}
        Aceleração y = {b.aceleração_y}

        Velocidade x = {b.velocidade_x}
        Velocidade y = {b.velocidade_y}

        Posição = {b.posicao}
        '''
        print(informaçoes)


    b.desenhar(tela)
    terra.desenhar(tela)
    
    pygame.display.update()
