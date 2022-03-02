import pygame
BLACK = [0, 0, 0]

class Player(pygame.sprite.Sprite):
    """ This class represents the main character Player """       
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("saucer.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = 900 / 2      
        self.speed = [0.5, -0.5] 

    def update(self):
        """ Actualize player's location """       
        pos = pygame.mouse.get_pos()      
        self.rect.x = pos[0]     
