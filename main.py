import pygame

# Előkészítés
pygame.init()

# Képernyő készítése
screen = pygame.display.set_mode((1200, 720))

# Assets
clock = pygame.time.Clock()
background_surface = pygame.image.load('assets/pics/background.png')
trash_surface = pygame.image.load('assets/pics/trash.png')
folder1_surface = pygame.image.load('assets/pics/folder1.png')
folder2_surface = pygame.image.load('assets/pics/folder2.png')
folder3_surface = pygame.image.load('assets/pics/folder3.png')
folder4_surface = pygame.image.load('assets/pics/folder4.png')
text1_surface = pygame.image.load('assets/pics/txt1.png')
text2_surface = pygame.image.load('assets/pics/txt2.png')
text3_surface = pygame.image.load('assets/pics/txt3.png')

# Cím és Ikon
pygame.display.set_caption("rozsast50")
icon = pygame.image.load('assets/pics/icon.png')
pygame.display.set_icon(icon)

# Játék Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_surface,(0,0))
    screen.blit(trash_surface, (55, 40))
    screen.blit(folder1_surface, (50, 150))
    screen.blit(folder2_surface, (50, 250))
    screen.blit(folder3_surface, (50, 350))
    screen.blit(folder4_surface, (50, 450))
    screen.blit(text1_surface, (250, 40))
    screen.blit(text2_surface, (400, 40))
    screen.blit(text3_surface, (550, 40))
    pygame.display.update()
    clock.tick(60)

    