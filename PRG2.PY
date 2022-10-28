# Simple pygame program

# Import and initialize the pygame library
import math
from typing import Counter
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
frames_per_second = 10

#Screen constants
SCREENSIZE_X = 500 #m
SCREENSIZE_Y = 250 #m

#Physics constants
GRAVITY = 9.81 #m/s^2

#Time settings
counter = 0
time_delay = 100
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, time_delay)

# Set up the drawing window
screen = pygame.display.set_mode([SCREENSIZE_X, SCREENSIZE_Y])


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'


class Canon(pygame.sprite.Sprite):

    def __init__(self):
        super(Canon, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.teta0 = math.pi/3              #!!!!!!!!!!!!!!!!!
        self.speed0 = 70 #m/s               #!!!!!!!!!!!!!!!!!
        self.counter = 0           #!!!!!!!!!!!!!!!!!

    def X_coord(self,t):
        return self.speed0*math.cos(self.teta0)*t
    
    def Y_coord(self,t):
        return SCREENSIZE_Y -(-GRAVITY*(t**2)/2 + self.speed0*math.sin(self.teta0)*t)

    #Rocket position
    def update(self):
        self.counter += 1
        self.rect.center = (self.X_coord(self.counter), self.Y_coord(self.counter))

# Instantiate canon
canon = Canon()

# Run until the user asks to quit
running = True

while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        elif event.type == timer_event:
            #changes rocket position
            canon.update()    #!!!!!!!!!!!!!!!!!!!!!!!!
            
        elif event.type == pygame.QUIT:
            running = False

    # Fill the background with Green
    screen.fill((76, 175, 80))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (250, 250, 250), (10, SCREENSIZE_Y -10), 5)

    # Draw the player on the screen
    screen.blit(canon.surf, canon.rect)

    # update the display
    clock.tick(frames_per_second)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
