import pygame
import settings

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
clock = pygame.time.Clock()

# ===== CLASSES DANS LE MAIN (IMPORTANT) =====

class Player:
    def __init__(self):
        self.x = 350
        self.y = 250
        self.size = 50
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.size, self.size))


class Coin:
    def __init__(self):
        import random
        self.x = random.randint(20, 760)
        self.y = random.randint(20, 560)
        self.size = 15

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 215, 0), (self.x, self.y), self.size)

# ===== GAME =====

player = Player()
coin = Coin()
score = 0

running = True

while running:
    clock.tick(settings.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    if abs(player.x - coin.x) < 30 and abs(player.y - coin.y) < 30:
        score += 1
        coin = Coin()

    screen.fill(settings.WHITE)

    player.draw(screen)
    coin.draw(screen)

    pygame.display.set_caption(f"Score: {score}")
    pygame.display.update()

pygame.quit()