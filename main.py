import random
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0

    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    shots: pygame.sprite.Group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for current_updatable in updatable:
            current_updatable.update(dt)

        for current_asteroid in asteroids:
            if player.collides_with(current_asteroid):
                print("Game over!")
                return

            for current_shot in shots:
                if current_shot.collides_with(current_asteroid):
                    current_asteroid.kill()

                    if current_asteroid.radius > ASTEROID_MIN_RADIUS:
                        new_radius = current_asteroid.radius - ASTEROID_MIN_RADIUS
                        random_angle = random.uniform(20, 50)
                        asteroid1_velocity = current_asteroid.velocity.rotate(
                            random_angle
                        )
                        asteroid2_velocity = current_asteroid.velocity.rotate(
                            -random_angle
                        )

                        asteroid_field.spawn(
                            new_radius, current_asteroid.position, asteroid1_velocity
                        )
                        asteroid_field.spawn(
                            new_radius, current_asteroid.position, asteroid2_velocity
                        )
                    current_shot.kill()

        for current_drawable in drawable:
            current_drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
