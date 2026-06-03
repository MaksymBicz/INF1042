import pygame
import random
import os
from settings import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Obstacle:

    def __init__(self):
        self.image = pygame.image.load(
            os.path.join(BASE_DIR, "assets", "trash.png")
        ).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect  = self.image.get_rect()

        self.rect.x = random.randint(0, WIDTH  - 50)
        self.rect.y = random.randint(-500, -100)

        self.speed = OBSTACLE_SPEED

    def respawn(self):
        self.rect.y = random.randint(-500, -100)
        self.rect.x = random.randint(0, WIDTH - 50)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.respawn()

    def draw(self, screen):
        screen.blit(self.image, self.rect)