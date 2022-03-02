import pygame
from game.artefacts import Artifact
BLACK = [0, 0, 0]
class Gema(Artifact, pygame.sprite.Sprite):
    """ This class represents the gems"""
    def __init__(self):
        super().__init__() 
        # self.image = pygame.image.load("gem.png").convert()
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect()

    def earn_points(self, score):        
        return score + 1         
