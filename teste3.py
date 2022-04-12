import pygame
from pygame.locals import *

from corpos import Bola
from uteis import *

pygame.init()

ALTURA = LARGURA = 600
tela = pygame.display.set_mode((ALTURA, LARGURA))

b = Bola((50, 50), 10)
terra = Bola((300, 300), 50, (0,0,255), 1000000)


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
        b.velocidade_x = b.velocidade_y = 0


    if colisao_circulo(b, terra):
        b.aceleração_x = b.aceleração_y = 0
        b.velocidade_x = b.velocidade_y = 0
    
    else:
        forca_g = calc_forca_gravitacional(b, terra)
        angulo = descobrir_angulo((b.posicao[0] - terra.posicao[0], b.posicao[1] - terra.posicao[1]))
        fx, fy = dividir_forca(forca_g, angulo)
        
        b.aceleração_x = fx/b.massa
        b.aceleração_y = fy/b.massa 


    b.desenhar(tela)
    terra.desenhar(tela)
    
    pygame.display.update()
