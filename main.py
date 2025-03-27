import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    """ The main function """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0, 0, 0)
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color, rect=None, special_flags=0)
        player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()
