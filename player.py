import pygame

class Player:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.score = 0

    def flap(self):
        self.velocity.y = -10

    def move_left(self):
        self.velocity.x = -5

    def move_right(self):
        self.velocity.x = 5

    def update(self):
        self.position += self.velocity
        self.velocity.y += 1  # Gravity effect

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.position.x), int(self.position.y)), 10)

    def collides_with(self, other):
        return self.position.distance_to(other.position) < 20
