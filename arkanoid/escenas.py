import pygame as pg
from . import FPS, ANCHO, ALTO
from .entidades import Raqueta, Bola, Ladrillo

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
        fuente = pg.font.Font("resources/fonts/CabinSketch-Bold.ttf", 45)
        self.textito = fuente.render("Pulsa <SPC> para comenzar", True, (0,0,0))
        self.anchoTexto = self.textito.get_width()


    def bucle_principal(self):
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
            self.pantalla.blit(self.textito, ((ANCHO - self.anchoTexto) // 2, 640))
            pg.display.flip()
        


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.fondo =pg.image.load("resources/images/background.jpg")
        self.todos = pg.sprite.Group()
        self.player = Raqueta(midbottom=(ANCHO // 2, ALTO - 15) )
        self.bola = Bola(center = (ANCHO // 3, ALTO // 2 - 200))
        self.puntos = 0

        self.ladrillos = pg.sprite.Group()
        for f in range(3):
            for c in range(6):
                ladrillo = Ladrillo(c * 90 + 30, f * 30 + 10)
                self.ladrillos.add(ladrillo)

        self.todos.add(self.ladrillos, self.bola, self.player)

    def bucle_principal(self):
        vidas = 3
        while vidas > 0:
            dt = self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

            self.todos.update(dt)

            self.bola.comprobar_colision(self.player)

            tocados = pg.sprite.spritecollide(self.bola, self.ladrillos, True)
            if len(tocados) > 0:
                self.bola.delta_y *= -1
                self.puntos += len(tocados) * 5
                print(self.puntos)

            
            if not self.bola.viva:
                vidas -= 1
                self.bola.viva = True

            self.pantalla.blit(self.fondo, (0, 0))
            self.todos.draw(self.pantalla)


            pg.display.flip()


class Records(Escena):
    def bucle_principal(self):
        print("soy records")

