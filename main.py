import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))  # screen size
pygame.display.set_caption("giga game")
pygame.display.set_icon(pygame.image.load('images/Sprite-0001.png'))

player = pygame.image.load('images/chel 1.png')
player_x = 300
player_y = 150
player_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    screen.fill((146, 138, 138))

    screen.blit(player, (player_x, player_y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_x -= player_speed
            if event.key == pygame.K_d:
                player_x += player_speed
            if event.key == pygame.K_w:
                player_y -= player_speed
            if event.key == pygame.K_s:
                player_y += player_speed


        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



