# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame.time import Clock
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    while True:
        screen.fill((0,0,0))
        dt = game_clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    screen.display.flip()

if __name__ == "__main__":
    main()
