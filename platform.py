import pygame

class Platform:
    def __init__(self, x, y, stability=100):
        self.position = pygame.Vector2(x, y)
        self.stability = stability

    def update(self):
        # Platforms may become unstable over time
        self.stability -= 0.1
        if self.stability < 0:
            self.stability = 0

    def draw(self, screen):
        color = (0, 255, 0) if self.stability > 50 else (255, 0, 0)
        pygame.draw.rect(screen, color, (self.position.x, self.position.y, 50, 10))

    def collides_with(self, other):
        return (self.position.x < other.position.x < self.position.x + 50 and
                self.position.y < other.position.y < self.position.y + 10)
