import pygame

class Bola:
    def __init__(self, p, raio, cor=(255,0,0), massa=1):
        self.posicao = p
        self.raio = raio
        self.cor = cor

        self.massa = massa

        self.velocidade_x = 0
        self.velocidade_y = 0

        self.aceleração_x = 0
        self.aceleração_y = 0

    def parar_corpo(self):
        self.aceleração_x = 0
        self.aceleração_y = 0
        self.velocidade_x = 0
        self.velocidade_y = 0

    def calc_posicao(self):
        self.velocidade_x += self.aceleração_x
        self.velocidade_y += self.aceleração_y
        self.posicao = (self.posicao[0] + self.velocidade_x, self.posicao[1] + self.velocidade_y)

    def desenhar(self, tela):
        self.calc_posicao()
        pygame.draw.circle(tela, self.cor, self.posicao, self.raio)


class Planeta(pygame.sprite.Sprite):
    def __init__(self, posicao, raio, massa=1, sprite=str):
        pygame.sprite.Sprite.__init__(self)
        self.posicao = posicao
        self.raio = raio

        self.massa = massa

        self.velocidade_x = 0
        self.velocidade_y = 0
        self.aceleração_x = 0
        self.aceleração_y = 0

        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (raio*2, raio*2))
        self.rect = self.image.get_rect()
        self.rect.center = self.posicao

    def calc_posicao(self):
        self.velocidade_x += self.aceleração_x
        self.velocidade_y += self.aceleração_y
        self.posicao = (self.posicao[0] + self.velocidade_x, self.posicao[1] + self.velocidade_y)

    def parar_corpo(self):
        self.aceleração_x = 0
        self.aceleração_y = 0
        self.velocidade_x = 0
        self.velocidade_y = 0

    def update(self):
        self.calc_posicao()
        self.rect.center = self.posicao
