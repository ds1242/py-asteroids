import pygame
from constants import *
from player import *
from asteroids import *

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # infinite loop for now for the game
    while running:
        # loop to poll and
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
                
        for obj in updatable:
            obj.update(dt)

        # fill the screen with a color to wipe away previous frame
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()