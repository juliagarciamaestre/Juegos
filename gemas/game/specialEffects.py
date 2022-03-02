import pygame 
dimensions = [900, 700] 
screen = pygame.display.set_mode(dimensions)
class SpecialEffects:
    def __init__(self):
         self.backg = ""
         self.music = ""
         self.sound_rock = ""
         self.sound_gem = ""   

    def load_backgrounds(self):
        self.backg = pygame.image.load("space_background.jpg")
        pygame.image.load("space_background.jpg").convert() 
        screen.blit(self.backg, [0, 0])

    def backg_music(self):
        self.music = pygame.mixer.music.load("plumbum-rain.wav")
        pygame.mixer.music.play()

    def sound_col_rock(self):
        self.sound_rock = pygame.mixer.Sound("kretopi__synthweapon-003.wav")
        self.sound_rock.play()

    def sound_col_gem(self):
        self.sound_gem = pygame.mixer.Sound("got_point.mp3")
        self.sound_gem.play()
