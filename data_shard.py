import pygame

class DataShard:
    def __init__(self, x, y, value=10):
        self.position = pygame.Vector2(x, y)
        self.value = value

    def update(self):
        pass  # Data shards are static, no need to update position

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.position.x), int(self.position.y)), 5)

    def collides_with(self, other):
        return self.position.distance_to(other.position) < 10
