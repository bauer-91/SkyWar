import sys
from builtins import print

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('background1-'))
        self.entity_list.append(EntityFactory.get_entity('player'))
        self.timeout = 20000
        pygame.time.set_timer(EVENT_ENEMY, 5000)

    def run(self):
        pygame.mixer_music.load(f'asset/level1.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('enemy'))

            self.level_text(14, f'LEVEL 1 - Timeout: {self.timeout / 1000 :.1f}s', (0, 255, 200), (10, 5))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Pixelify Sans Bold", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
