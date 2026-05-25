class Player:
    def __init__(self):
        self.x = 350
        self.y = 250
        self.size = 50
        self.speed = 5

    def move(self, keys):
        import pygame

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.size, self.size))