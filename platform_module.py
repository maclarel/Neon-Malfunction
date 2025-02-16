import pygame

class Platform:
    def __init__(self, x, y, stability=100):
        self.position = pygame.Vector2(x, y)
        self.stability = stability
        self.rect = pygame.Rect(x, y, 50, 10)

    def update(self):
        # Platforms may become unstable over time
        self.stability -= 0.05
        if self.stability < 0:
            self.stability = 0
        self.rect.topleft = (self.position.x, self.position.y)

    def draw(self, screen):
        color = (0, 255, 0) if self.stability > 50 else (255, 0, 0)
        pygame.draw.rect(screen, color, (self.position.x, self.position.y, 50, 10))

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)
