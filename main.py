import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    # infinite loop for now for the game
    while running:
        # loop to poll and quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill the screen with a color to wipe away previous frame
        screen.fill("black")
        



if __name__ == "__main__":
    main()