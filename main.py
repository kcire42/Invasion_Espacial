import pygame

#Inicializar pygame
pygame.init()

#Crear pantalla
display = pygame.display.set_mode((800,600))

#Titulo de Icono
pygame.display.set_caption("Space Inveder")
ruta_icono = "/Users/kcire/Library/CloudStorage/GoogleDrive-erickcarrillo2807@gmail.com/Mi unidad/Programacion/Python/16 dias de python/Invasion_Espacial/Img/alien.png"
icono = pygame.image.load(ruta_icono)
pygame.display.set_icon(icono)

#Jugador
ruta_player = "Img/rocket-ship.png"
player_img = pygame.image.load(ruta_player)
player_x = 368
player_y = 536
def player (x,y):
    display.blit(player_img,(x,y))


#Loop del Juego
se_ejecuta = True
while se_ejecuta:

    #RGB fondo de la pantalla
    display.fill((23,132,255))
    for evento in pygame.event.get():
        #cerrar pantalla
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #interaccion teclado
        keys = pygame.key.get_pressed()
        #TURBO
        if keys[pygame.K_LSHIFT]:
            base_speed = 10
        else:
            base_speed = 5
        #Movimiento
        if keys[pygame.K_a]:
            player_x -= base_speed
        if keys[pygame.K_d]:
            player_x += base_speed
        if keys[pygame.K_w]:
            player_y -= base_speed
        if keys[pygame.K_s]:
            player_y += base_speed

    # mantener dentro de bordes 
    if player_x <=0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    if player_y >= 536:
        player_y = 536
    elif player_y <=0:
        player_y = 0
    player(player_x,player_y)
    #actualizar pantalla
    pygame.display.update()


