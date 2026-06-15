from code.Const import ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.x = float(self.rect.centerx)

    def move(self, ):
        self.x -= ENTITY_SPEED[self.name]
        self.rect.centerx = round(self.x)

        if self.rect.right <= 0:
            self.rect.left = 576
            self.x = self.rect.centerx
