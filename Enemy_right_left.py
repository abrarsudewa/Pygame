# Simple pygame program

# Import and initialize the pygame library
import pygame # type: ignore
pygame.init()

width = 800
height = 500

# Set up the drawing window
screen = pygame.display.set_mode([width, height])

x = 0
y = 100

right = True
left = False

speed =  0.1

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if right == True:
        if x < 800:
            x = x + 1
        if x == 800:
            right = False
            left = True

    if left == True:
        if x <= 800:
            x = x - 1
        if x == 0:
            right = True
            left = False


    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()