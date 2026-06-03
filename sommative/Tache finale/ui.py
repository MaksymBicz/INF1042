import pygame
from settings import *

pygame.font.init()

_font       = pygame.font.SysFont("Arial", 30)
_small_font = pygame.font.SysFont("Arial", 22)


def draw_ui(screen, score, lives, level):
    screen.blit(_font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(_font.render(f"Lives: {lives}", True, WHITE), (10, 50))
    screen.blit(_font.render(f"Level: {level}", True, WHITE), (10, 90))


def draw_level_up(screen, level):
    surf = pygame.font.SysFont("Arial", 52, bold=True).render(
        f"LEVEL {level}!", True, YELLOW
    )
    rect = surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(surf, rect)