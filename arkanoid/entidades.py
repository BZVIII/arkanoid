import pygame as pg
from pygame.sprite import Sprite
from . import ANCHO, ALTO

class Raqueta(Sprite):
    disfraces = "electric00.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)

    def update(self):
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.rect.x -= 5

        if self.rect.left <= 0:
            self.rect.left = 0

        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rect.x +=5

        if self.rect.right >= ANCHO:
            self.rect.right = ANCHO


class Bola(Sprite):
    disfraces = "ball1.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)
        self.delta_x = 5
        self.delta_y = 5
        self.viva = True
        self.posicion_inicial = kwargs

    def update(self, raqueta):
        self.rect.x += self.delta_x
        if self.rect.x <=0 or self.rect.right >= ANCHO:
            self.delta_x *= -1

        self.rect.y += self.delta_y
        if self.rect.y <=0:
            self.delta_y *= -1

        if self.rect.bottom >= ALTO:
            self.viva = False
            self.rect = self.image.get_rect(**self.posicion_inicial)

 
    def comprobar_colision(self, otro):
        if self.rect.right >= otro.rect.left and self.rect.left <= otro.rect.right and \
           self.rect.bottom >= otro.rect.top and self.rect.top <= otro.rect.bottom:
           self.delta_y *= -1




