import pygame
import random

class Enemy:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.choice([-0.5, 0.5]), random.choice([-0.5, 0.5]))
        self.rect = pygame.Rect(x, y, 20, 20)
        self.value = 10

    def update(self):
        self.position += self.velocity
        if self.position.x < 0 or self.position.x > 800:
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > 600:
            self.velocity.y *= -1
        self.rect.topleft = (self.position.x, self.position.y)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), 10)

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)
