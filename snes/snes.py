import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, height = 256, 256
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('templates/control.png').convert()
frameReact = pygame.Rect((0, 0), (width, height))

crosshair = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshair, pygame.Color("white"), (5, 5), 10, 0)

crosshairb = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshairb, pygame.Color("red"), (5, 5), 5, 0)

triggerL = pygame.surface.Surface((10, 10))
pygame.draw.circle(triggerL, pygame.Color("yellow"), (5, 5), 5, 0)

triggerR = pygame.surface.Surface((10, 10))
pygame.draw.circle(triggerR, pygame.Color("yellow"), (5, 5), 5, 0)

select = pygame.surface.Surface((10, 10))
pygame.draw.circle(select, pygame.Color("green"), (5, 5), 5, 0)

start = pygame.surface.Surface((10, 10))
pygame.draw.circle(start, pygame.Color("green"), (5, 5), 5, 0)




while True:

    pygame.event.pump()

    screen.blit(background_image, (0,0))

    Keys=pygame.key.get_pressed()

    if Keys[pygame.K_x]: screen.blit(crosshair, (197, 103))#botton x    del control
    if Keys[pygame.K_c]: screen.blit(crosshair, (172, 123))#botton y    del control
    if Keys[pygame.K_v]: screen.blit(crosshair, (222, 123))#botton a    del control
    if Keys[pygame.K_z]: screen.blit(crosshair, (197, 140))#botton b    del control

    """ if Keys[pygame.K_k]: screen.blit(crosshair, (220, 60))
    if Keys[pygame.K_l]: screen.blit(crosshair, (200, 100))
    if Keys[pygame.K_j]: screen.blit(crosshair, (200, 100))
    if Keys[pygame.K_i]: screen.blit(crosshair, (200, 100))"""

    if Keys[pygame.K_f]: screen.blit(triggerL, (195, 68))
    if Keys[pygame.K_a]: screen.blit(triggerR, (50, 68))

    if Keys[pygame.K_s]: screen.blit(select, (100, 130))
    if Keys[pygame.K_d]: screen.blit(start, (130, 130))

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0

    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0



    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(crosshairb, ((x*15)+55-5, (y*15)+128-5))

    pygame.display.flip()

    clk.tick(40)