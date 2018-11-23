import pygame
from fruta import Fruta

class Cesta(pygame.sprite.Sprite):#cria o objeto lixeira
    def _init_(self, x, y ):
        super()._init_()
        self.image = pygame.image.load('cesta.png').convert_alpha()#objeto com imagem
        self.rect = self.image.get_rect()#armazena o retângulo da imagem em rect
        self.rect.x = x #posiciona a imagem nas coordenadas passadas como parâmetro
        self.rect.y = y
        self.x1 = x
        self.y1 = y

    ''''#método para movimentar o bloco
    def mover(self, x, y):
        self.rect.x = x
        self.rect.y = y'''

    def mover(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def andarDireita(self):
        self.rect.x += 1

    #método para movimentar o bloco
