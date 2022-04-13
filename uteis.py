import pygame

####Configurando a fonte####
pygame.font.init()
fonte_padrao = pygame.font.get_default_font()
fonte_info = pygame.font.SysFont(fonte_padrao, 18)


def escrever_info(informacoes, tela, px):
    for i in range(len(informacoes)):
        text = fonte_info.render(informacoes[i], 1, (255,255,255))
        tela.blit(text, ((px, i*14)))