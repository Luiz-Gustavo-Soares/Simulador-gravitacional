import pygame
from pygame.locals import *

from corpos import Bola
from calculos import *
from uteis import *

pygame.init()

ALTURA = 600
LARGURA = 1000
tela = pygame.display.set_mode((LARGURA, ALTURA))


bolas = []
terra = Bola((LARGURA/2, ALTURA/2), 50, (0,0,255), 1000000)

velocidade_inicial =  5

clock = pygame.time.Clock()
mouse_destravado = True

while True:
    clock.tick(100)
    tela.fill((0,0,0))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()

        elif evento.type == KEYDOWN:
            if evento.key == K_l:
                bolas = []

            elif evento.key == K_q:
                pygame.quit()
                quit()
            
            elif evento.key == K_PAGEUP:
                velocidade_inicial += 0.5

            elif evento.key == K_PAGEDOWN:
                velocidade_inicial -= 0.5

    if pygame.mouse.get_pressed()[0] and mouse_destravado:
        bolas.append(Bola(pygame.mouse.get_pos(), 6))
        bolas[-1].velocidade_x = velocidade_inicial

        mouse_destravado = False
    elif not pygame.mouse.get_pressed()[0]:
        mouse_destravado = True


    for b in bolas:

        if colisao_circulo(b, terra):
            b.parar_corpo()
        
        else:
            forca_g = calc_forca_gravitacional(b, terra)
            fx, fy = dividir_forca(forca_g, b.posicao, terra.posicao)
            
            b.aceleração_x = fx/b.massa * -1
            b.aceleração_y = fy/b.massa * -1

        b.desenhar(tela)

    terra.desenhar(tela)

    informacoes = (f"Velocidade Inicial = {velocidade_inicial}", f"Quantidade de esferas = {len(bolas)}")
    escrever_info(informacoes, tela, LARGURA-150)

    pygame.display.update()
