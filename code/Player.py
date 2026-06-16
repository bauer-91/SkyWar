import pygame

from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def update(self):
        pass

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.y > 0:
            self.rect.centery -= 5
        if pressed_key[pygame.K_DOWN] and self.rect.y < 287:
            self.rect.centery += 5
        if pressed_key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.centerx -= 5
        if pressed_key[pygame.K_RIGHT] and self.rect.x < 516:
            self.rect.centerx += 5
        pass

    def shoot(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_SPACE]:
            return PlayerShot(
                'playerShot',
                (
                    self.rect.right - 41,
                    self.rect.centery - 30
                )
            )