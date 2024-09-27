import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

press = False

# bullet data
x_bullet = -10
y_bullet = 250
speed_bullet = 1
radius = 10

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (x_bullet, y_bullet), radius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        press = True
    if press == True:
        x_bullet += speed_bullet
    if x_bullet >= 510:
        press = False
        x_bullet = -10

    pygame.display.flip()

pygame.quit()