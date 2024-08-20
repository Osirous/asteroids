import pygame
import random
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def draw(self, screen):
        color = self.random_color()
        pygame.draw.circle(screen, color, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt