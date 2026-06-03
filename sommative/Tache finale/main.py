import pygame
import random
import os

from settings import *
from player   import Player
from fish     import Fish
from obstacle import Obstacle
from level    import LevelSystem
from ui       import draw_ui, draw_level_up

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fishing Adventure")

clock = pygame.time.Clock()

background = pygame.image.load(os.path.join(BASE_DIR, "assets", "water.png"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

font       = pygame.font.SysFont("Arial", 56, bold=True)
small_font = pygame.font.SysFont("Arial", 32)


def new_game():
    player       = Player()
    fish_list    = [Fish() for _ in range(5)]
    obstacles    = [Obstacle() for _ in range(3)]
    level_system = LevelSystem()
    score        = 0
    lives        = 3
    return player, fish_list, obstacles, level_system, score, lives


player, fish_list, obstacles, level_system, score, lives = new_game()

running        = True
game_over      = False
level_up_timer = 0

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                player, fish_list, obstacles, level_system, score, lives = new_game()
                game_over = False

    if not game_over:

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.update()

        for fish in fish_list:
            fish.update()
            if player.rect.colliderect(fish.rect):
                score += 1
                fish.respawn()

        for obstacle in obstacles:
            obstacle.update()
            if player.rect.colliderect(obstacle.rect):
                if player.hit():
                    lives -= 1
                    obstacle.respawn()

        level_system.update(score)

        if level_system.level_changed:
            level_up_timer = 120
            new_speed_f = level_system.fish_speed()
            new_speed_o = level_system.obstacle_speed()
            for fish in fish_list:
                fish.set_speed(new_speed_f)
            for obs in obstacles:
                obs.speed = new_speed_o
            if len(fish_list) < 10:
                fish_list.append(Fish(base_speed=new_speed_f))

        if level_up_timer > 0:
            level_up_timer -= 1

        if lives <= 0:
            game_over = True

    screen.blit(background, (0, 0))

    if not game_over:

        pygame.draw.line(
            screen, WHITE,
            (player.rect.centerx, player.rect.bottom),
            (player.rect.centerx, player.rect.bottom + 80),
            3
        )

        player.draw(screen)

        for fish in fish_list:
            fish.draw(screen)

        for obstacle in obstacles:
            obstacle.draw(screen)

        draw_ui(screen, score, lives, level_system.level)

        if level_up_timer > 0:
            draw_level_up(screen, level_system.level)

    else:

        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))

        go_surf = font.render("GAME OVER", True, RED)
        go_rect = go_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))
        screen.blit(go_surf, go_rect)

        fs_surf = small_font.render(f"Final Score: {score}", True, WHITE)
        fs_rect = fs_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(fs_surf, fs_rect)

        rs_surf = small_font.render("Press R to Restart", True, WHITE)
        rs_rect = rs_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
        screen.blit(rs_surf, rs_rect)

    pygame.display.update()

pygame.quit()