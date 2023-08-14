import sys,pygame

class Ball():
    def __init__(self,pos_x,pos_y):
        self.pos_x=pos_x
        self.pos_y=pos_y

    def get_x(self):
        return self.pos_x

    def get_y(self):
        return self.pos_y
        
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

    def set_coord_x(self,x):
        self.coord.x=x

    def set_coord_y(self,y):
        self.coord.y=y
    
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#Gestion des balles
list_ball=[Ball(screen.get_width()/2,screen.get_height()/2)]
list_pos=[]
for ball in list_ball:
    list_pos.append([pygame.Vector2(ball.get_x(),ball.get_y()),1,1])

#Gestion des rackets
racket_1=racket(screen.get_width()/5,screen.get_height()/2,100,30)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    #Mouvement des rackets
    pygame.draw.line(screen,"red",racket_1.get_coord_bottom(),racket_1.get_coord_top(),racket_1.get_width())


    #Mouvement des balles
    for player_pos in list_pos :
        pygame.draw.circle(screen, "red", player_pos[0], 30)
        #Déplacement selon x
        if player_pos[0].x<screen.get_width()-30 and player_pos[1]==1: 
            player_pos[0].x+=300*dt
        elif player_pos[0].x>=screen.get_width()-30 and player_pos[1]==1 :
            player_pos[1]=-1
        elif player_pos[0].x>=screen.get_width()-30 and player_pos[1]==-1 :
            player_pos[0].x-=300*dt
        elif player_pos[0].x>0+30 and player_pos[1]==-1: 
            player_pos[0].x-=300*dt
        elif player_pos[0].x<=0+30 and player_pos[1]==-1: 
            player_pos[1]=1
    
        #Déplacement selon y
        if player_pos[0].y<screen.get_height()-30 and player_pos[2]==1: 
            player_pos[0].y+=300*dt
        elif player_pos[0].y>=screen.get_height()-30 and player_pos[2]==1 :
            player_pos[2]=-1
        elif player_pos[0].y>=screen.get_height()-30 and player_pos[2]==-1 :
            player_pos[0].y-=300*dt
        elif player_pos[0].y>0+30 and player_pos[2]==-1: 
            player_pos[0].y-=300*dt
        elif player_pos[0].y<=0+30 and player_pos[2]==-1: 
            player_pos[2]=1
    


    

    

   

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()