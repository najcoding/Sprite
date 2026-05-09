import pygame
import sys


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Rectangles with Controls")


clock = pygame.time.Clock()


RECT_WIDTH = 60
RECT_HEIGHT = 40


player_rect = pygame.Rect(100, 100, RECT_WIDTH, RECT_HEIGHT)


static_rect = pygame.Rect(400, 300, RECT_WIDTH, RECT_HEIGHT)


PLAYER_SPEED = 5


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_rect.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_rect.y += PLAYER_SPEED

    
    player_rect.x = max(0, min(player_rect.x, SCREEN_WIDTH - RECT_WIDTH))
    player_rect.y = max(0, min(player_rect.y, SCREEN_HEIGHT - RECT_HEIGHT))

    
    screen.fill(WHITE)  
    pygame.draw.rect(screen, RED, player_rect)   
    pygame.draw.rect(screen, BLUE, static_rect)  

    
    pygame.display.flip()

    clock.tick(60)
