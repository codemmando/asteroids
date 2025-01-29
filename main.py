import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = {shots, updatable, drawable}
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = time.tick(60) / 1000
        screen.fill(0000)

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        for item in updatable:
            item.update(dt)
        
        for item in asteroids:
            if item.collision(player):
                print("Game over!")
                return

        for item in shots:
            for asteroid in asteroids:
                if item.collision(asteroid):
                    item.kill()
                    asteroid.split()
                    
        

        time.tick(60)

if __name__ == "__main__":
    main()
