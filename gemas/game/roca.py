import pygame
from game.artefacts import Artifact
BLACK = [0, 0, 0]

class Roca(Artifact, pygame.sprite.Sprite):
    """ This class represents the rocs"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rock.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def lose_points(self, score):        
        return score - 1     
