import pygame

from code.Menu import Menu
from code.Level import Level

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == 0:
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                quit()
