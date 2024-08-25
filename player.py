import pygame
from constants import (
    COLOR_WHITE,
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    """

    Attributes:
        position:
        rotation:
    """

    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.rotation: float = 0
        self.shot_cooldown: float = 0

    def triangle(self):
        """

        Args:
            self ():

        Returns:

        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        """

        Args:
            screen:
        """
        pygame.draw.polygon(screen, COLOR_WHITE, self.triangle(), 2)

    def rotate(self, dt: float) -> None:
        """

        Args:
            dt:
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        """

        Args:
            dt:
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shot_cooldown -= dt

    def move(self, dt: float) -> None:
        """

        Args:
            dt:
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self) -> None:
        if self.shot_cooldown <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            )
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
