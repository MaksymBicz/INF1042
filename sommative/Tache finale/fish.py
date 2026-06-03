import pygame
import random
import os
from settings import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Fish:

    def __init__(self, base_speed=None):
        self.image = pygame.image.load(
            os.path.join(BASE_DIR, "assets", "fish.png")
        ).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.rect  = self.image.get_rect()

        self.rect.x = random.randint(0, WIDTH - 60)
        self.rect.y = random.randint(-300, -50)

        self._base_speed = base_speed if base_speed is not None else FISH_SPEED
        self.speed       = self._base_speed + random.uniform(-0.5, 0.5)

    def set_speed(self, base_speed):
        self._base_speed = base_speed
        self.speed       = base_speed + random.uniform(-0.5, 0.5)

    def respawn(self):
        self.rect.y = random.randint(-300, -50)
        self.rect.x = random.randint(0, WIDTH - 60)
        self.speed  = self._base_speed + random.uniform(-0.5, 0.5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.respawn()

    def draw(self, screen):
        screen.blit(self.image, self.rect)