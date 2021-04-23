import pygame
import os
from ship import *

#class layar
class Window:
    def __init__(self, besar_layar): 
        # inisialisasi pygame
        pygame.init()
        self.lebar = besar_layar[0]
        self.tinggi = besar_layar[1]
        # membuat object layar dengan sebesar {besar_layar}
        self.layar = pygame.display.set_mode(besar_layar)


class Game:
    def __init__(self, window):
        self.__dt = 0
        self.window = window
        self.ship = Ship((50, 50), 100, "ship.png", (100, 200), 5, 2)
    

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.update()
            self.draw()
            self.__dt = self.delta_time(clock.tick(30))

    def draw(self):
        self.window.layar.fill((0, 0, 0))

        self.ship.draw(self.window)

        pygame.display.flip()

    def update(self):
        events = pygame.event.get()
        for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
        
        self.ship.update(self.__dt)

    # mendapatkan jarak waktu antara dua frame dalam satuan detik
    def delta_time(self, time_between):
        return time_between / 1000.0