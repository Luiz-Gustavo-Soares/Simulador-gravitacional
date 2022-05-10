import pygame

#Configurando a fonte#
pygame.font.init()
fonte_padrao = pygame.font.get_default_font()
fonte_info = pygame.font.SysFont(fonte_padrao, 18)


def escrever_info(informacoes, tela=object, largura_tela=int):
    '''
    -> Imprime algum texto no canto supeiro direito da tela do pygame.
    :param informacoes: texto a ser escrito.
    :param tela: tela do pygame a ser colocada a informação.
    :param largura_tela: largura da tela a ser impreça.
    :return: None
    '''

    for i in range(len(informacoes)):
        tamanho = 0
        for j in informacoes:
            if len(j) > tamanho:
                tamanho = len(j)
        tamanho *= 6
        text = fonte_info.render(informacoes[i], 1, (255,255,255))
        tela.blit(text, ((largura_tela-tamanho, i*14)))
    
    pygame.draw.line(tela, (255,255,255), (largura_tela-tamanho-5, 0), (largura_tela-tamanho-5, len(informacoes)*14))
