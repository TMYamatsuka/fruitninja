import pygame
from random import randrange

class Fruta(pygame.sprite.Sprite):
    def __init__(self,imagem):
        super().__init__()
        self.numero = 0
        self.image = pygame.image.load(imagem).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, 500)
        self.rect.y = -200
        self.y1 =  self.rect.y
        self.x1 = self.rect.x


    def cair(self):
        self.rect.y += randrange(1, 3)
        self.y1 =  self.rect.y
        self.x1 = self.rect.x

    def mover(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def morrer(self):
        self.kill()
