import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialization Section
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroid = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroid, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    #player instance(put player things before this. updatable and drawable were below this which caused the player to stop displaying on screen...)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Gameplay Loop
    while True:
        # Close button makes the loop stop here.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # drawing the screen black    
        screen.fill((0,0,0))

        # update player
        for obj in updatable:
            obj.update(dt)
        
        for aster in asteroid:
            if aster.collision_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision_with(aster):
                    aster.split()
                    shot.kill()

        # render player
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limiting frames per second to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
