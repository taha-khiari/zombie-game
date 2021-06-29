import pygame
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self, game):

        super().__init__()
        self.game= game
        self.health = 100
        self.max_health=100
        self.attack = 0.1
        self.velocity= random.randint(1,2)
        self.image= pygame.image.load("assets/koo.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 510

    def damage(self,amount):
        self.health -= amount
        if self.health<=0 :

            self.rect.x=1000 + random.randint(0,300)
            self.health= self.max_health


    def updat_health_bar(self, surface):
        bar_color= (111, 210, 46 )
        bar_color_a= (60,63,60)
        bar_position= (self.rect.x+40,self.rect.y-20, self.health, 5)
        bar_pos_a=(self.rect.x+40,self.rect.y-20, self.max_health, 5)

        pygame.draw.rect(surface, bar_color_a,bar_pos_a)
        pygame.draw.rect(surface, bar_color, bar_position)
    def move(self):
        if not self.game.check_collision(self,self.game.all_players):

            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
