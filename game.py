import pygame
import random
from player import Player
from enemy import Enemy
from data_shard import DataShard
from neon_grid import NeonGrid

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
enemies = [Enemy(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(5)]
data_shards = [DataShard(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(10)]
platforms = [Platform(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(5)]
neon_grid = NeonGrid()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    # Collision detection
    for enemy in enemies:
        if player.collides_with(enemy):
            if player.position.y < enemy.position.y:
                enemies.remove(enemy)
            else:
                running = False

    for data_shard in data_shards:
        if player.collides_with(data_shard):
            player.score += data_shard.value
            data_shards.remove(data_shard)

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

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
