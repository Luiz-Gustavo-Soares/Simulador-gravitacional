import pygame
from pygame.locals import *

from functions.corpos import *
from functions.calculos import *
from functions.uteis import *

pygame.init()

ALTURA = 600
LARGURA = 1000
pygame.display.set_caption("Simulação Gravitacional - 02")
tela = pygame.display.set_mode((LARGURA, ALTURA))

todas_as_sprites = pygame.sprite.Group() 

terra = Planeta(posicao=(LARGURA/2, ALTURA/2), raio=50, sprite='./img/corpos/terra.png', massa=1000000)
satelite = Planeta(posicao=(60, 60), raio=20, sprite='./img/corpos/satelite.png', massa=100)
todas_as_sprites.add(terra)
todas_as_sprites.add(satelite)

fundo = pygame.image.load('./img/fundos/01.jpg')
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

lancar_c_mouse = True
parar_corpo = False
mostrar_informacoes = True
velocidade_inicial = [0, 0]

clock = pygame.time.Clock()
while True:
    clock.tick(50)
    tela.fill((0,0,0))
    tela.blit(fundo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()
        
        elif evento.type == KEYDOWN:
            if evento.key == K_p:
                parar_corpo = False if parar_corpo else True

            elif evento.key == K_l:
                lancar_c_mouse = False if lancar_c_mouse else True

            elif evento.key == K_i:
                mostrar_informacoes = False if mostrar_informacoes else True
            
            elif evento.key == K_LEFT:
                velocidade_inicial[0] -= 0.5
            elif evento.key == K_RIGHT:
                velocidade_inicial[0] += 0.5
            elif evento.key == K_UP:
                velocidade_inicial[1] += 0.5
            elif evento.key == K_DOWN:
                velocidade_inicial[1] -= 0.5

    if pygame.mouse.get_pressed()[0]:
        satelite.posicao = pygame.mouse.get_pos()

        if lancar_c_mouse:
            vel = list(pygame.mouse.get_rel())
            v_max = 6

            for i in range(2):
                if vel[i] > v_max:
                    vel[i] = v_max
                elif vel[i] < -v_max:
                    vel[i] = -v_max
        else:
            vel = velocidade_inicial
            
        satelite.velocidade_x = vel[0]
        satelite.velocidade_y = vel[1]
    


    forca_g = calc_forca_gravitacional(satelite, terra)
    fx, fy = dividir_forca(forca_g, satelite.posicao, terra.posicao)
        
    if colisao_circulo(satelite, terra) or parar_corpo:
        satelite.parar_corpo()
    
    else:
        satelite.aceleração_x = fx/satelite.massa * -1
        satelite.aceleração_y = fy/satelite.massa * -1

    print(forca_g)
    informacoes = ('***SATELITE***',
     f'Velocidade X/Y: ({satelite.velocidade_x:.3f} {satelite.velocidade_y:.3f})',
     f'Aceleração X/Y: ({satelite.aceleração_x:.3f} {satelite.aceleração_y:.3f})', 
     f'Força Gravitacional: {forca_g:.4f}', 
     f'Raio: {satelite.raio}',
     f'Massa: {satelite.massa}', 
     '',
     '***CONFIGURAÇÕES***',
     f'Velocidade Inicial X/Y: {velocidade_inicial}',
     f'Lançar c/ o mouse: {lancar_c_mouse}',
     f'Corpo parado: {parar_corpo}' )
    
    if mostrar_informacoes:
        escrever_info(informacoes=informacoes, tela=tela, largura_tela=LARGURA)

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()
