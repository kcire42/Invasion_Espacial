import pygame

#Inicializar pygame
pygame.init()

#Crear pantalla
display = pygame.display.set_mode((800,600))

#Loop del Juego
se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

