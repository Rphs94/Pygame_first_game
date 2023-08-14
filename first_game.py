import sys,pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
speed_x=1
speed_y=1
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 30)

    #Déplacement selon x
    if player_pos.x<screen.get_width()-30 and speed_x==1: 
        player_pos.x+=300*dt
    elif player_pos.x>=screen.get_width()-30 and speed_x==1 :
        speed_x=-1
    elif player_pos.x>=screen.get_width()-30 and speed_x==-1 :
        player_pos.x-=300*dt
    elif player_pos.x>0+30 and speed_x==-1: 
        player_pos.x-=300*dt
    elif player_pos.x<=0+30 and speed_x==-1: 
        speed_x=1
    
    #Déplacement selon y
    if player_pos.y<screen.get_height()-30 and speed_y==1: 
        player_pos.y+=300*dt
    elif player_pos.y>=screen.get_height()-30 and speed_y==1 :
        speed_y=-1
    elif player_pos.y>=screen.get_height()-30 and speed_y==-1 :
        player_pos.y-=300*dt
    elif player_pos.y>0+30 and speed_y==-1: 
        player_pos.y-=300*dt
    elif player_pos.y<=0+30 and speed_y==-1: 
        speed_y=1
    

    

    

   

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()