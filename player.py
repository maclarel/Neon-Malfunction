import pygame
from enemy import Enemy

class Player:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.score = 0
        self.rect = pygame.Rect(x, y, 20, 20)

    def flap(self):
        self.velocity.y = -5

    def move_left(self):
        self.velocity.x = -2.5

    def move_right(self):
        self.velocity.x = 2.5

    def update(self):
        self.position += self.velocity
        self.velocity.y += 0.5  # Gravity effect
        self.rect.topleft = (self.position.x, self.position.y)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.position.x), int(self.position.y)), 10)

    def collides_with(self, other):
        if self.rect.colliderect(other.rect):
            return True
        return False
