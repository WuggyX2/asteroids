import pygame
from  typing_extensions import Self

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):


    def __init__(self, x: int, y: int, radius: float):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self: Self, screen: pygame.Surface):
        # sub-classes must override
        pass

    def update(self: Self, dt: float):
        # sub-classes must override
        pass

    def collides_with(self: Self, other: Self) -> bool:
        return self.position.distance_to(other.position) < self.radius + other.radius
