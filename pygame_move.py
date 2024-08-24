# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 500])

x = 50
y = 100
width = 20
height = 20
vel = 1

# Menggunakan pygame clock untuk mengontrol FPS
# clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:
    # Membatasi kecepatan loop ke 60 FPS
    # clock.tick(60)
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        x -= vel

    if keys[pygame.K_d]:
        x += vel

    if keys[pygame.K_w]:
        y -= vel

    if keys[pygame.K_s]:
        y += vel

    # Fill the background with black
    screen.fill((0, 0, 0))

    # Draw a solid red rectangle
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

