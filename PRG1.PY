# Simple pygame program

# Import and initialize the pygame library
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

SCREENSIZE_X = 250
SCREENSIZE_Y = 250

# Set up the drawing window
screen = pygame.display.set_mode([SCREENSIZE_X, SCREENSIZE_Y])


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 10))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys == K_UP:
            self.rect.move_ip(0, -5)
        if pressed_keys == K_DOWN:
            self.rect.move_ip(0, 5)
        if pressed_keys == K_LEFT:
            self.rect.move_ip(-5, 0)
        if pressed_keys == K_RIGHT:
            self.rect.move_ip(5, 0)
    

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREENSIZE_X:
            self.rect.right = SCREENSIZE_X
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREENSIZE_Y:
            self.rect.bottom = SCREENSIZE_Y

# Instantiate player. Right now, this is just a rectangle.
player = Player()


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
            if event.key == K_UP or K_DOWN or K_LEFT or K_RIGHT:
                player.update(event.key)

        elif event.type == pygame.QUIT:
            running = False
    
    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Fill the background with Green
    screen.fill((76, 175, 80))


    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (250, 250, 250), (10, SCREENSIZE_Y -10), 5)

   # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()