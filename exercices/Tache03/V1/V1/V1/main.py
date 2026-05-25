import pygame
import settings
from player import Player

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Mon Jeu")

clock = pygame.time.Clock()

player = Player()

running = True

while running:
    clock.tick(settings.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill(settings.WHITE)
    player.draw(screen)

    pygame.display.update()

pygame.quit()