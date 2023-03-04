import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, height = 1003, 458
screen = pygame.display.set_mode(size)

background_image = pygame.image.load('./snes.png').convert()
frameRect = pygame.Rect((0, 0), (width, height))

# ABXY
crosshair = pygame.surface.Surface((30,30))
pygame.draw.circle(crosshair, pygame.Color("white"), (15,15), 15, 0)

# WASD
crosshairB = pygame.surface.Surface((30,30))
pygame.draw.circle(crosshairB, pygame.Color("red"), (15, 15), 15, 0)

# LR - START SELECT
crosshairN = pygame.surface.Surface((30,30))
pygame.draw.circle(crosshairN, pygame.Color("magenta"), (15, 15), 15, 0)

while True:

    pygame.event.pump()
    screen.blit(background_image, (0,0))

    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_p]: screen.blit(crosshair, (855, 200)) # [A]
    if Keys[pygame.K_l]: screen.blit(crosshair, (763, 268)) # [B]
    if Keys[pygame.K_o]: screen.blit(crosshair, (763, 125)) # [X]
    if Keys[pygame.K_k]: screen.blit(crosshair, (673, 200)) # [Y]

    if Keys[pygame.K_w]: screen.blit(crosshairB, (212, 144)) # [UP]
    if Keys[pygame.K_s]: screen.blit(crosshairB, (212, 251)) # [DW]
    if Keys[pygame.K_a]: screen.blit(crosshairB, (158, 198)) # [LF]
    if Keys[pygame.K_d]: screen.blit(crosshairB, (266, 198)) # [RG]

    if Keys[pygame.K_q]: screen.blit(crosshairN, (212, 1)) # [L]
    if Keys[pygame.K_e]: screen.blit(crosshairN, (763, 1)) # [R]

    if Keys[pygame.K_n]: screen.blit(crosshairN, (408, 225)) # [SEL]
    if Keys[pygame.K_m]: screen.blit(crosshairN, (509, 225)) # [STR]

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()
    clk.tick(40)