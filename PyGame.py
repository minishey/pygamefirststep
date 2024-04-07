import pygame
from pygame import Surface, Rect

W_WIDTH = 576
W_HEIGHT = 324
# Inicializar o Módulo do PyGame
pygame.init()
print('Setup Start')
# Criação de janela do pygame
screen: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

# Carregar imagem e gerar uma superfície
bg_surface: Surface = pygame.image.load('./Asset/bg.png').convert_alpha()
p1_surface: Surface = pygame.image.load('./Asset/p1.png').convert_alpha()

# Obter o Retângulo da superfície
bg_rect: Rect = bg_surface.get_rect(left=0, top=0)
p1_rect: Rect = p1_surface.get_rect(left=100, top=100)

# Desenhar na janela (screen)
screen.blit(source=bg_surface, dest=bg_rect)
screen.blit(source=p1_surface, dest=p1_rect)

# Atualizar a janela
pygame.display.flip()

# Colocar um relógio no nosso jogo
clock = pygame.time.Clock()


# Carregar música e deixar ela tocando
pygame.mixer_music.load('./Asset/ChopinGrandValse.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.3)
print('Setup End')
print('Loop Start')
while True:
    clock.tick(140)  # Esse loop está acontecendo 30 vezes por segundo
    #  print(f'{clock.get_fps() :.0f}')  # Executar o print do FPS
    screen.blit(source=bg_surface, dest=bg_rect)
    screen.blit(source=p1_surface, dest=p1_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Loop End...')
            pygame.quit()
            quit()
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        p1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        p1_rect.centery += 1
    if pressed_key[pygame.K_d]:
        p1_rect.centerx += 1
    if pressed_key[pygame.K_a]:
        p1_rect.centerx -= 1
        pass
#
