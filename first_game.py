import sys,pygame

class Ball():
    def __init__(self,pos_x,pos_y):
        self.coord=pygame.Vector2(pos_x,pos_y)
        self.speed_x=1
        self.speed_y=1

    def get_coord(self):
        return self.coord
    def get_x(self):
        return self.coord.x

    def get_y(self):
        return self.coord.y

    def get_speed_x(self):
        return self.speed_x
    
    def get_speed_y(self):
        return self.speed_y
    
    def set_x(self,x):
        self.coord.x=x

    def set_y(self,y):
        self.coord.y=y
    
    def set_speed_x(self,speed_x):
        self.speed_x=speed_x
    
    def set_speed_y(self,speed_y):
        self.speed_y=speed_y
    


class racket():

    def __init__(self,pos_x,pos_y,length,width):
        self.coord=pygame.Vector2(pos_x,pos_y)
        self.length=length
        self.width=width

    
    def get_coord_top(self):
        return (self.coord.x,self.coord.y+self.length)
    
        
    def get_coord_bottom(self):
        return (self.coord.x,self.coord.y-self.length)
    
    def get_width(self):
        return self.width

    def get_coord_y(self):
        return self.coord.y
    
    def get_coord_x(self):
        return self.coord.x

    def set_coord_y(self,y):
        self.coord.y=y


#Paramètres généraux
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
speed_racket=300
running = True
dt = 0

#Gestion des balles
list_ball=[Ball(screen.get_width()/2,screen.get_height()/2)]

#Gestion des rackets
racket_1=racket(screen.get_width()/10,screen.get_height()/2,100,30)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    #Mouvement des rackets
    pygame.draw.line(screen,"white",racket_1.get_coord_bottom(),racket_1.get_coord_top(),racket_1.get_width())
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        racket_1.set_coord_y(racket_1.get_coord_y()-speed_racket*dt)
    elif keys[pygame.K_s]:
        racket_1.set_coord_y(racket_1.get_coord_y()+speed_racket*dt)




    #Mouvement des balles
    for ball in list_ball :
        pygame.draw.circle(screen, "white", ball.get_coord(), 30)

    #Interaction de la balle avec le mur de droite
        if ball.get_x()<screen.get_width()-30 and ball.get_speed_x()==1: 
            ball.set_x(ball.get_x()+300*dt)
        elif ball.get_x()>=screen.get_width()-30 and ball.get_speed_x()==1 :
            ball.set_speed_x(-1)
        elif ball.get_x()>=screen.get_width()-30 and ball.get_speed_x()==-1 :
            ball.set_x(ball.get_x()-300*dt)
        elif ball.get_x()>0+30 and ball.get_speed_x()==-1: 
            ball.set_x(ball.get_x()-300*dt)
        elif ball.get_x()<=0+30 and ball.get_speed_x()==-1: 
            ball.set_speed_x(1)
    #Interaction de la balle avec la raquette gauche 
    
        if abs(ball.get_x()-racket_1.get_coord_x())<=30 and not (ball.get_y()>racket_1.get_coord_top()[1] or ball.get_y()<racket_1.get_coord_bottom()[1]) and ball.get_speed_x()==-1: 
            ball.set_speed_x(1)
        if abs(ball.get_x()-racket_1.get_coord_x())<=30 and not (ball.get_y()>racket_1.get_coord_top()[1] or ball.get_y()<racket_1.get_coord_bottom()[1]) and ball.get_speed_x()==1: 
            ball.set_x(ball.get_x()+300*dt)
    
    


    
    #Interaction de la balle avec les surfaces verticales
        if ball.get_y()<screen.get_height()-30 and ball.get_speed_y()==1: 
            ball.set_y(ball.get_y()+300*dt)
        elif ball.get_y()>=screen.get_height()-30 and ball.get_speed_y()==1 :
            ball.set_speed_y(-1)
        elif ball.get_y()>=screen.get_height()-30 and ball.get_speed_y()==-1 :
            ball.set_y(ball.get_y()-300*dt)
        elif ball.get_y()>0+30 and ball.get_speed_y()==-1: 
            ball.set_y(ball.get_y()-300*dt)
        elif ball.get_y()<=0+30 and ball.get_speed_y()==-1: 
            ball.set_speed_y(1)
    


    

    

   

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()