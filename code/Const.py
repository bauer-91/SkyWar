import pygame

ENTITY_SPEED = {
    'background1-1': 0,
    'background1-2': 0.1,
    'background1-3': 0.5,
    'background1-4': 1,
    'enemy': 2,
}

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_HEALTH = {
    'player': 100,
    'enemy': 50,
    'background1-1': 999,
    'background1-2': 999,
    'background1-3': 999,
    'background1-4': 999,
}