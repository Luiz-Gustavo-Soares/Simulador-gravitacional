import pygame

####Configurando a fonte####
pygame.font.init()
fonte_padrao = pygame.font.get_default_font()
fonte_info = pygame.font.SysFont(fonte_padrao, 18)


def escrever_info(informacoes, tela, pos_x):
    for i in range(len(informacoes)):
        tamanho = 0
        for j in informacoes:
            if len(j) > tamanho:
                tamanho = len(j)
        tamanho *= 6
        text = fonte_info.render(informacoes[i], 1, (255,255,255))
        tela.blit(text, ((pos_x-tamanho, i*14)))