import pygame
from pygame.locals import *

size = width, height =(1200,1200)
road_w = int(width/1.6)
roadline_w = int(width/80)

pygame.init()

running = True
screen = pygame.display.set_mode(size)
name = pygame.display.set_caption("Need for d7k") 
screen.fill((112,245,89))

# draw graphics
pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2-road_w/2,0,road_w, height)
)
# yellow line
pygame.draw.rect(
    screen,
    (255,240,69),
    (width/2 - roadline_w/2  , 0 , roadline_w , height)
)
# white lines
pygame.draw.rect(
    screen,
    (255,255,255),
    (width/2 - road_w/2 + roadline_w*2, 0 , roadline_w , height)
)

pygame.draw.rect(
    screen,
    (255,255,255),
    (width/2 + road_w/2 - roadline_w*3 , 0 , roadline_w , height)
)

pygame.display.update()

#load cars

redCar = pygame.image.load("whitecar.png")
redCar_loc = redCar.get_rect()
redCar_loc.center = width/2 + road_w/4 , height * 0.8 



while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(redCar , redCar_loc)  # modify the ratio of the carsize    
    pygame.display.update()




pygame.quit()