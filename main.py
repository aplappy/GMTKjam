import pygame

pygame.init()
screen= pygame.display.set_mode((600,300)) # screen size
pygame.display.set_caption("giga game")
pygame.display.set_icon(pygame.image.load('images/Sprite-0001.png'))

player = pygame.image.load('images/chel 1.png')
player_x = 300
player_y = 150
player_speed = 5



running = True
while running:

    pygame.display.update()

    screen.blit(player, (player_x, 150))



    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_x += player_speed
    elif keys[pygame.K_a]:
        player_x -= player_speed





    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


