import pygame as pg
from . import FPS, ANCHO

class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()
    
    def bucle_principal(self):
        pass
    
class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.logo = pg.image.load("resources/images/arkanoid_name.png")
        fuente = pg.font.Font("resources/fonts/CabinSketch-Bold.ttf", 80)
        self.textito = fuente.render("Pulsa <SPC> para comenzar", True, (0,0,0))
        self.anchoTexto = self.textito.get_width()


    def bucle_principal(self):
        print("soy portada")
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True

            self.pantalla.fill((80, 80, 255))
            self.pantalla.blit(self.logo, (140, 140))
            self.pantalla.blit(self.textito, ((ANCHO - self.anchoTexto) // 2, 340))
            pg.display.flip()
        


class Partida(Escena):
    def bucle_principal(self):
        print("soy partida")

class Records(Escena):
    def bucle_principal(self):
        print("soy records")

