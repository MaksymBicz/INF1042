import pygame
import random

class Coin:
    def __init__(self):
        self.x = random.randint(20, 760)
        self.y = random.randint(20, 560)
        self.size = 15

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 215, 0), (self.x, self.y), self.size)