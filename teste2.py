import pygame
from pygame.locals import *

from corpos import Bola
from uteis import *

pygame.init()

ALTURA = LARGURA = 600
tela = pygame.display.set_mode((ALTURA, LARGURA))

bolas = [Bola((50, 50), 10)]


terra = Bola((300, 300), 50, (0,0,255), 100000000)




clock = pygame.time.Clock()
while True:
    clock.tick(50)
    tela.fill((0,0,0))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()


    if pygame.mouse.get_pressed()[0]:
        bolas.append(Bola(pygame.mouse.get_pos(), 10, massa=100))

    for b in bolas:
        if colisao_circulo(b, terra):
            b.aceleração_x = b.aceleração_y = 0
            b.velocidade_x = b.velocidade_y = 0

        forca_g = calc_forca_gravitacional(b, terra)
        b.aceleração_x = b.aceleração_y = forca_g
        b.desenhar(tela)


    terra.desenhar(tela)
    

    pygame.display.update()
