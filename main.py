import pygame
from constants import * 
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x, y)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))

        dt = clock.tick(60) / 1000

        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)
        
        
        pygame.display.flip()
        

if __name__ == "__main__":
    main()