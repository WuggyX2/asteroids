import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS,COLOR_WHITE

class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, 2)


    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
