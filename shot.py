from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

# Base Class for Shot object (bullet)
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
