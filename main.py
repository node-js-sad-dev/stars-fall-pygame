import pygame

import sys
from random import randrange

from settings import Settings
from star import Star


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.settings: Settings = Settings()

        self.screen: pygame.Surface = pygame.display.set_mode((self.settings.program_w, self.settings.program_h))
        pygame.display.set_caption("Star sky game")

        self.stars = []

        self.falling_stars = []

        self._create_stars()

    def _create_stars(self):
        stars_count = randrange(80, 99)

        for star in range(stars_count):
            self.stars.append(Star(self))

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill((0, 0, 0))

        for star in self.stars:
            star.draw_star()

        for star in self.falling_stars:
            star.update()
            star.draw_star()
            if (star.center_y + star.radius / 2) >= self.settings.program_h:
                self.falling_stars.remove(star)

        print(self.falling_stars)

        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and len(self.stars) > 0:
                rand_index = randrange(0, len(self.stars))
                self.falling_stars.append(self.stars[rand_index])
                self.stars.pop(rand_index)


if __name__ == '__main__':
    game = Game()
    game.run_game()
