import pygame
import random
class Comet(pygame.sprite.Sprite):

    def __init__(self,comet_event):
        super().__init__()
        self.image=pygame.image.load("assets/comet.png")
        self.rect=self.image.get_rect()
        self.velocity= random.randint(1,3)
        self.rect.x = random.randint(20,100)
        self.rect.y= - random.randint(0,800)
        self.comet_event = comet_event
    def remove(self):
        self.comet_event.all_comet.remove(self )
    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 500:
            print("sol")
            self.remove()