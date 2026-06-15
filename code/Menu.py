import pygame.image
from pygame import Surface, Rect
from pygame.font import Font


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.music.load('./asset/menu.wav')
        pygame.mixer.music.play(-1)
        menu_option = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, "Sky War", (180, 235, 255), (288, 140))
            for i in range(1):
                if menu_option == 0:
                    self.menu_text(20, "INICIAR JOGO", (0, 255, 200), (288, 200))
                    self.menu_text(20, "SAIR", (180, 235, 255), (288, 220))
                else:
                    self.menu_text(20, "INICIAR JOGO", (180, 235, 255), (288, 200))
                    self.menu_text(20, "SAIR", (0, 255, 200), (288, 220))
            self.menu_text(15, "COMANDOS DO MENU - Selecionar opção: Setas direcionais / Selecionar: Enter", (180, 235, 255), (288, 270))
            self.menu_text(15, "COMANDOS DO JOGO - Mover nave: Setas direcionais / Atirar: Espaço", (180, 235, 255), (288, 280))
            self.menu_text(15, "Desenvolvido por Matias Bauer - RU:5221804", (180, 235, 255), (288, 310))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option != 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option != 0:
                            menu_option -= 1
                        else:
                            menu_option = 1
                    if event.key == pygame.K_RETURN:
                        return menu_option

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Pixelify Sans Bold", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
