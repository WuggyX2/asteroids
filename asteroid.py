"""
Represents an asteroid in the game.

"""
import pygame
from typing_extensions import Self
from constants import COLOR_WHITE

from circleshape import CircleShape


class Asteroid(CircleShape):
    """

    """

    def __init__(self, x: int, y: int, radius: float):
        super().__init__(x, y, radius)



    def draw(self: Self, screen:  pygame.Surface) -> None:
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, 2)

    def update(self: Self, dt: float) -> None:
        self.position += self.velocity * dt
