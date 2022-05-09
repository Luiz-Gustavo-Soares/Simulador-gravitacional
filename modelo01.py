import pygame
from pygame.locals import *

from functions.corpos import Bola
from functions.calculos import *
from functions.uteis import *

pygame.init()

ALTURA = 600
LARGURA = 1000
pygame.display.set_caption("Simulação Gravitacional - 01")
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
        b.parar_corpo()
    
    else:
        forca_g = calc_forca_gravitacional(b, terra)
        fx, fy = dividir_forca(forca_g, b.posicao, terra.posicao)
        
        b.aceleração_x = fx/b.massa * -1
        b.aceleração_y = fy/b.massa * -1

    informacoes = (f'Força G = {forca_g:.4f}', f'Aceleração X = {b.aceleração_x:.4f}', f'Aceleraçao Y = {b.aceleração_y:.4f}', f'Velocidade x = {b.velocidade_x:.4f}', f'Velocidade y = {b.velocidade_y:.4f}', f'Posição x/y = {b.posicao[0]:.2f}, {b.posicao[1]:.2f}')
    escrever_info(informacoes, tela, LARGURA)

    b.desenhar(tela)
    terra.desenhar(tela)
    
    pygame.display.update()
