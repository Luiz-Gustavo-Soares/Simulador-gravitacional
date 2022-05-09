from copy import copy
import pygame
from pygame.locals import *

from corpos import *
from calculos import *
from uteis import *

pygame.init()

ALTURA = 600
LARGURA = 1000
pygame.display.set_caption("Simulação Gravitacional - 02")
tela = pygame.display.set_mode((LARGURA, ALTURA))

todas_as_sprites = pygame.sprite.Group() 

terra = Planeta(posicao=(LARGURA/2, ALTURA/2), raio=50, sprite='./img/terra.png', massa=1000000)
satelite = Planeta(posicao=(60, 60), raio=20, sprite='./img/satelite.png')
todas_as_sprites.add(terra)
todas_as_sprites.add(satelite)

clock = pygame.time.Clock()
while True:
    clock.tick(100)
    tela.fill((0,0,0))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()

    if pygame.mouse.get_pressed()[0]:
        satelite.posicao = pygame.mouse.get_pos()
        satelite.velocidade_x = 0
        satelite.velocidade_y = 0
    

    
    if colisao_circulo(satelite, terra):
        satelite.parar_corpo()
    
    else:
        forca_g = calc_forca_gravitacional(satelite, terra)
        fx, fy = dividir_forca(forca_g, satelite.posicao, terra.posicao)
        
        satelite.aceleração_x = fx/satelite.massa * -1
        satelite.aceleração_y = fy/satelite.massa * -1


    informacoes = ('***SATELITE***',
     f'Velocidade X/Y ({satelite.velocidade_x:.3f} {satelite.velocidade_y:.3f})',
     f'Aceleração X/Y ({satelite.aceleração_x:.3f} {satelite.aceleração_y:.3f})', 
     f'Força Gravitacional {forca_g:.4f}')
    
    escrever_info(informacoes=informacoes, tela=tela, largura_tela=LARGURA)

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()
