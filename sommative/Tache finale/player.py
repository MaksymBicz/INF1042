import pygame
import os
from settings import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Player:

    def __init__(self):
        self.image = pygame.image.load(
            os.path.join(BASE_DIR, "assets", "boat.png")
        ).convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.rect  = self.image.get_rect()

        self.rect.centerx = WIDTH  // 2
        self.rect.y        = HEIGHT - 120

        self.speed = PLAYER_SPEED

        self.invincible          = False
        self.invincibility_timer = 0

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        self.rect.left  = max(self.rect.left,  0)
        self.rect.right = min(self.rect.right, WIDTH)

    def update(self):
        if self.invincible:
            self.invincibility_timer -= 1
            if self.invincibility_timer <= 0:
                self.invincible = False

    def hit(self):
        if self.invincible:
            return False
        self.invincible          = True
        self.invincibility_timer = INVINCIBILITY_FRAMES
        return True

    def draw(self, screen):
        if self.invincible and (self.invincibility_timer // 6) % 2 == 0:
            return
        screen.blit(self.image, self.rect)