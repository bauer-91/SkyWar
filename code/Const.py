import pygame

ENTITY_SPEED = {
    'background1-1': 0,
    'background1-2': 0.1,
    'background1-3': 0.5,
    'background1-4': 1,
    'enemy': 2,
    'playerShot': 3,
    'enemyShot': 4,
}

EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_ENEMY_SHOT = pygame.USEREVENT + 2

ENTITY_HEALTH = {
    'player': 100,
    'enemy': 50,
    'background1-1': 999,
    'background1-2': 999,
    'background1-3': 999,
    'background1-4': 999,
    'playerShot': 999,
    'enemyShot': 999,
}