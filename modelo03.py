import pygame
from pygame.locals import *

from corpos import Bola, Terra
from calculos import *
from uteis import *

pygame.init()

ALTURA = 600
LARGURA = 1000
pygame.display.set_caption("Simulação Gravitacional - 02")
tela = pygame.display.set_mode((LARGURA, ALTURA))


todas_as_sprites = pygame.sprite.Group() 
terra = Terra(posicao=(LARGURA/2, ALTURA/2))
todas_as_sprites.add(terra)

clock = pygame.time.Clock()
while True:
    clock.tick(100)
    tela.fill((0,0,0))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
