import pygame, random

class Artifact(pygame.sprite.Sprite):
    """ This class represents the Artifacts like gems and rocks """
    def __init__(self):
        super().__init__() 
        self.image = ""
        self.color = " " 
        self.rect = ""

    def reset_pos(self):        
        self.rect.y = random.randrange(-300, 50)
        self.rect.x = random.randrange(0, 900)

    def update(self):       
        self.rect.y += 4
        if self.rect.y > 900:
            self.reset_pos()
