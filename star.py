import pygame
from pygame.sprite import Sprite
from random import randrange, choices


class Star(Sprite):
    def __init__(self, game):
        super().__init__()

        directions = ['left', 'right']

        self.game = game
        self.screen: pygame.Surface = game.screen
        self.settings = self.game.settings

        self.radius = randrange(2, 4)

        self.color = (randrange(1, 255), randrange(1, 255), randrange(1, 255))
        self.center_x = randrange(self.radius // 2, self.settings.program_w - self.radius // 2)
        self.center_y = randrange(self.radius // 2, self.settings.program_h - self.radius // 2)

        self.x_iterator = 0

        self.angle = randrange(1, 5)

        self.move_direction = choices(directions)[0]

    def update(self):
        self.center_y += 1
        if self.x_iterator % 4 == 0:
            if self.move_direction == 'left':
                self.center_x -= self.angle
            else:
                self.center_x += self.angle
        self.x_iterator += 1

    def draw_star(self):
        pygame.draw.circle(self.screen, self.color, (self.center_x, self.center_y), self.radius)
