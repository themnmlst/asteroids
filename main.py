import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    """ The main function """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color, rect=None, special_flags=0)
        pygame.display.flip()

if __name__ == "__main__":
    main()
