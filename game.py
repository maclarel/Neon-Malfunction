import pygame
import random
from player import Player
from enemy import Enemy
from data_shard import DataShard
from neon_grid import NeonGrid
from platform_module import Platform

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Neon Malfunction")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Create game objects
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
initial_enemy_count = 5
enemies = [Enemy(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(initial_enemy_count)]
data_shards = [DataShard(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), value=2) for _ in range(10)]
platforms = [Platform(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(5)]
neon_grid = NeonGrid()

# Global variable to store persistent score
persistent_score = 0

def game_over_screen(final_score):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("GAME OVER", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2 - 50))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Final Score: {final_score}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - score_text.get_height() // 2))

    play_again_text = font.render("Press R to Play Again", True, WHITE)
    screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, SCREEN_HEIGHT // 2 - play_again_text.get_height() // 2 + 50))

    quit_text = font.render("Press Q to Quit", True, WHITE)
    screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 - quit_text.get_height() // 2 + 100))

    pygame.display.flip()

def level_up_screen(current_score):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    level_up_text = font.render("LEVEL UP!", True, WHITE)
    screen.blit(level_up_text, (SCREEN_WIDTH // 2 - level_up_text.get_width() // 2, SCREEN_HEIGHT // 2 - level_up_text.get_height() // 2 - 50))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Current Score: {current_score}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - score_text.get_height() // 2))

    next_level_text = font.render("Press N to Advance to Next Level", True, WHITE)
    screen.blit(next_level_text, (SCREEN_WIDTH // 2 - next_level_text.get_width() // 2, SCREEN_HEIGHT // 2 - next_level_text.get_height() // 2 + 50))

    pygame.display.flip()

def reset_game(increase_enemies=1):
    global player, enemies, data_shards, platforms, neon_grid, initial_enemy_count, persistent_score
    persistent_score = player.score
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    player.score = persistent_score
    initial_enemy_count = max(1, int(initial_enemy_count * (1 + increase_enemies)))
    enemies = [Enemy(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(initial_enemy_count)]
    data_shards = [DataShard(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), value=2) for _ in range(10)]
    platforms = [Platform(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(5)]
    neon_grid = NeonGrid()

# Game loop
running = True
game_over = False
level_up = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reset_game()
            game_over = False
        if keys[pygame.K_q]:
            running = False
        continue

    if level_up:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            reset_game(increase_enemies=0.2)
            level_up = False
        continue

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.flap()
    if keys[pygame.K_a]:
        player.move_left()
    if keys[pygame.K_d]:
        player.move_right()

    # Update game objects
    player.update()
    for enemy in enemies:
        enemy.update()
    for data_shard in data_shards:
        data_shard.update()
    for platform in platforms:
        platform.update()
    neon_grid.update()

    # Check if player touches the boundaries
    if player.position.x < 0 or player.position.x > SCREEN_WIDTH or player.position.y < 0 or player.position.y > SCREEN_HEIGHT:
        game_over = True

    # Collision detection
    for enemy in enemies:
        if player.collides_with(enemy):
            if player.position.y < enemy.position.y:
                enemies.remove(enemy)
            else:
                game_over = True

    for data_shard in data_shards:
        if player.collides_with(data_shard):
            player.score += data_shard.value
            data_shards.remove(data_shard)

    for platform in platforms:
        if player.collides_with(platform):
            player.position.y = platform.position.y - player.rect.height

    for element in neon_grid.elements:
        if player.collides_with(element):
            player.position.y = element.position.y - player.rect.height

    # Check if all enemies and data shards are collected
    if not enemies and not data_shards:
        level_up = True

    # Draw everything
    screen.fill(BLACK)
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for data_shard in data_shards:
        data_shard.draw(screen)
    for platform in platforms:
        platform.draw(screen)
    neon_grid.draw(screen)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {player.score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

    if game_over:
        game_over_screen(player.score)
    elif level_up:
        level_up_screen(player.score)

# Quit Pygame
pygame.quit()
