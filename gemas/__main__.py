import pygame
import random
from game.artefacts import Artifact
from game.gema import Gema
from game.roca import Roca
from game.message import Message
from game.player import Player
from game.specialEffects import SpecialEffects

pygame.init()
pygame.mouse.set_visible(0) 

BLUE = [12, 44, 146]
GREEN = [46, 189, 20]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]

#My screen
dimensions = [900, 700] 
screen = pygame.display.set_mode(dimensions)

effects = SpecialEffects()
music = effects.backg_music() 

# This is a list of all the sprites.
lista_de_todos_los_sprites = pygame.sprite.Group() 
# This list represents each artifact in the game.
lista_artifacts = pygame.sprite.Group()
lista_gemas = pygame.sprite.Group()
lista_rocks = pygame.sprite.Group()

for i in range(60):
    gema =Gema() 
    # setting the gems' location 
    gema.rect.x = random.randrange(0, 900)
    gema.rect.y = random.randrange(-3500, 100)     
    lista_gemas.add(gema)
    lista_de_todos_los_sprites.add(gema)
    lista_artifacts.add(gema)

for i in range(60):
    rock = Roca() 
    # setting the rocks' location 
    rock.rect.x = random.randrange(0, 900)
    rock.rect.y = random.randrange(-3500, 100)     
    lista_rocks.add(rock)
    lista_de_todos_los_sprites.add(rock)
    lista_artifacts.add(rock)  

player = Player()
lista_de_todos_los_sprites.add(player)
reloj = pygame.time.Clock()
player.rect.y = 600
done = False

# -------- Instruction Page Loop -----------
while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            done = True

    # Limit to 60 frames per second
    reloj.tick(60)
    screen.fill(WHITE)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Main program loop
hecho = False
score = 0
while not hecho:                           

    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT: 
            hecho = True       

    """--- Game logical---""" 

    lista_de_todos_los_sprites.update()

    artifact = Artifact()          

    gem_hit = pygame.sprite.spritecollide(player, lista_gemas, True)
    rock_hit = pygame.sprite.spritecollide(player, lista_rocks, True)         

    for artifact in gem_hit:                                

            effects.sound_col_gem()            
            gema =Gema() 
            # setting the gems' location 
            gema.rect.x = random.randrange(0, 900)
            gema.rect.y = random.randrange(-3500, 50)     
            lista_gemas.add(gema)
            lista_de_todos_los_sprites.add(gema)
            lista_artifacts.add(gema)                   
            score -= 1   

    for artifact in rock_hit:           
            effects.sound_col_rock()  
            rock = Roca() 
            # setting the rocks' location 
            rock.rect.x = random.randrange(0, 900)
            rock.rect.y = random.randrange(-3500, 50)     
            lista_rocks.add(rock)
            lista_de_todos_los_sprites.add(rock)
            lista_artifacts.add(rock)
            score += 1 

    font = pygame.font.Font(None, 40)
    points = font.render('SCORE = '+str(score), 
    True, (200,200,200), (0,0,0) )                  
    rectanglePoints = points.get_rect()           
    rectanglePoints.left = 10                           
    rectanglePoints.top = 10        
    pygame.display.flip()

    screen.fill(WHITE)    

    backg = effects.load_backgrounds()   
    lista_de_todos_los_sprites.draw(screen)
    print_score = screen.blit(points, rectanglePoints)

    pygame.display.flip()

    reloj.tick(110)

pygame.quit() 
'''#################
from email import message
import pygame
import random

class Artifact(pygame.sprite.Sprite):
    """ This class represents the Artifacts like gems and rocks """
    def __init__(self):
        super().__init__() 
        self.image = " "
        self.color = " " 
        self.rect = ""

    def reset_pos(self):        
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, 900)
        
    def update(self):       
        self.rect.y += 1
        if self.rect.y > 900:
            self.reset_pos() 

class Gema(Artifact, pygame.sprite.Sprite):
    """ This class represents the gems"""
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface([10, 10])
        self.color = self.image.fill(RED)  
        self.rect = self.image.get_rect()        

class Roca(Gema, pygame.sprite.Sprite):
    """ This class represents the rocs"""
    def __init__(self):
        super().__init__()
        self._image =  pygame.Surface([10, 10]) 
        self.color = self.image.fill(GREEN)
    
    def earn_points(self, score):        
        return score + 1     
 
class Player(pygame.sprite.Sprite):
    """ This class represents the main character Player """       
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.image = pygame.Surface([10, 10])
             
        self.rect = self.image.get_rect()
        self.rect.centerx = 900 / 2
       #self.rect.centery = 700 / 2 
        self.speed = [0.5, -0.5] 
                 
    def update(self):
        """ Actualize player's location """       
        pos = pygame.mouse.get_pos()      
        self.rect.x = pos[0]     

class Message:
    def __init__(self):
        self.message = ""

        def colide_gem():
            self.message = "Hurrah! You got 1 point!"
            return self.message
    
        def colide_rock():
            self.message = "Ups! You lost 1 point!"
            return self.message
        
pygame.init()

BLUE = [12, 44, 146]
GREEN = [46, 189, 20]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]

#My screen
dimensions = [900, 700] 
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Greed Game")

# This is a list of all the sprites.
lista_de_todos_los_sprites = pygame.sprite.Group() 
# This list represents each artifact in the game.
lista_artifacts = pygame.sprite.Group()
lista_gemas = pygame.sprite.Group()
lista_rocks = pygame.sprite.Group()
 
for i in range(60):
    gema =Gema() 
    # setting the gems' location 
    gema.rect.x = random.randrange(0, 900)
    gema.rect.y = random.randrange(-3500, 50)     
    lista_gemas.add(gema)
    lista_de_todos_los_sprites.add(gema)
    lista_artifacts.add(gema)

for i in range(60):
    rock = Roca() 
    # setting the rocks' location 
    rock.rect.x = random.randrange(0, 900)
    rock.rect.y = random.randrange(-3500, 50)     
    lista_rocks.add(rock)
    lista_de_todos_los_sprites.add(rock)
    lista_artifacts.add(rock)  

player = Player()
lista_de_todos_los_sprites.add(player)

reloj = pygame.time.Clock()

score = 0
player.rect.y = 600
done = False

 
# -------- Instruction Page Loop -----------
while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            done = True
 
    # Set the screen background
    screen.fill(BLACK) 
   
    # Limit to 60 frames per second
    reloj.tick(60)
    screen.fill(WHITE)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Main program loop
hecho = False
while not hecho:
     
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT: 
            hecho = True        
            
    """--- Game logical---""" 
    
    lista_de_todos_los_sprites.update()

    artifact = Artifact()          
          
    gem_hit_list = pygame.sprite.spritecollide(player, lista_gemas, True)
    rock_hit_list = pygame.sprite.spritecollide(player, lista_rocks, True)         
                
    for artifact in gem_hit_list:                                
            lista_gemas.remove(gema)            
            lista_artifacts.remove(gema)          
            score + 1   
    
    for artifact in rock_hit_list:           
            lista_rocks.remove(rock)
            lista_artifacts.remove(rock)
            score - 1 
                                  
    fuente = pygame.font.Font(None, 30)
    points = fuente.render('SCORE '+str(score), 
    True, (200,200,200), (0,0,0) )                  
    rectanglePoints = points.get_rect()           
    rectanglePoints.left = 10                           
    rectanglePoints.top = 10                            

    pygame.display.flip()
    screen.fill(WHITE)          
      
    lista_de_todos_los_sprites.draw(screen)
    print_score = screen.blit(points, rectanglePoints)
    pygame.display.flip()
    
    reloj.tick(110)
   
pygame.quit()
'''
##########
'''
import pygame, sys,random
import pygame.event
import pygame.locals

pygame.init()       

ancho=700
alto=500        
white=(255,255,255)
color_gemas=(0,255,0)
color_rocas=(0,90,0)
##linea 13
#Coordenadas del jugador
cord_x=350
cord_y=450
#Velocidad del jugador
velocidad_x= 0
velocidad_y = 0

pygame.display.set_caption("Greed --||")
clock = pygame.time.Clock()
class Artifact:

    def __init__(self):
        self._position=[]
        self._center = ancho/2
        self._velocidad = 3
        self._ventana = pygame.display.set_mode((ancho, alto))        


    def relleno_position(self):
        for i in range(60):
            x=random.randint(1,700)
            y=random.randint(1,600)           
            self._position.append([x,y])                    
    
class Gema(Artifact):

    def __init__(self):
        super().__init__()
        self._gema="*"
        self._positionX=0
        self._positionY=0        
        
    def dibujar_gemas(self):
        self._ventana.fill(white)        
        for coordenada in self._position:
            pygame.draw.circle(self._ventana,color_gemas,(coordenada),7)
            #el cuatro es la velocidad o la cantidad de pixeles que avanzan los puntos de las coordenadas de las pelotitas que avanzaran hasta llegar al final de pantalla.
            coordenada[1]+=4
            #verifico que las gemas vuelvan a aparecen al llegar al final e la pantalla eje de las 'Y'
            if  coordenada[1] == 600 :
                coordenada[1] = 0
        
class Roca(Artifact):
    def __init__(self):
        super().__init__()
        self._rocas="O"

    def dibujar_rocas(self):        
        for coordenada in self._position:
            pygame.draw.circle(self._ventana,color_rocas,(coordenada),9)
            #el cuatro es la velocidad o la cantidad de pixeles que avanzan los puntos de las coordenadas de las pelotitas que avanzaran hasta llegar al final de pantalla.
            coordenada[1]+=4
            if  coordenada[1] == 596 :
                coordenada[1] = 0

class Player(Artifact):
    def __init__(self):
        super().__init__()
        
            
    def dibujar_player(self):
                
        pygame.draw.rect(self._ventana,(0,133,255),(cord_x, cord_y, 35 , 5), 0)
        

gema=Gema()
gema.relleno_position()
roca=Roca()
roca.relleno_position()
player=Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    #EVENTOS TECLADO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidad_x = -3
            if event.key == pygame.K_RIGHT:
                velocidad_x = 3

        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_LEFT:
                velocidad_x = 0
            if event.key == pygame.K_RIGHT:
                velocidad_x = 0

    

    #aumento la velocidad en 3 pixeles del player
    # cord_x += velocidad_x
    # if cord_x > 660 or cord_x < 0:
    #     #Invierte la velocidad
    #     velocidad_x *= -1
    
    #ventana.fill(white)
    cord_x += velocidad_x
    gema.dibujar_gemas()
    roca.dibujar_rocas()
    player.dibujar_player()
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
       
'''



       
