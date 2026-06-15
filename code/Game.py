import pygame

from code.Menu import Menu

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == 0:
                pass
            elif menu_return == 1:
                pass
            elif menu_return == 2:
                pygame.quit()
                quit()
