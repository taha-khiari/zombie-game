import pygame

from projectil import projectile

class player (pygame.sprite.Sprite):

    def __init__(self,game):

        super().__init__()
        self.game= game
        self.health= 100
        self.max_health=100
        self.attack=10
        self.velocity= 5
        self.all_projectiles = pygame.sprite.Group()
        self.image= pygame.image.load("assets/robot.png")
        self.rect= self.image.get_rect()
        self.rect.x= 30
        self.rect.y= 500

    def updat_health_bar(self, surface):
        bar_color= (111, 210, 46 )
        bar_color_a= (60,63,60)
        bar_position= (self.rect.x+50,self.rect.y+30, self.health, 5)
        bar_pos_a=(self.rect.x+50,self.rect.y+30, self.max_health, 5)

        pygame.draw.rect(surface, bar_color_a,bar_pos_a)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self,amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def launch_projectile(self):

        self.all_projectiles.add(projectile(self))

    def mouv_R(self):
        if not self.game.check_collision(self,self.game.all_monster):
            self.rect.x += self.velocity
    def mouv_L(self):
        self.rect.x -= self.velocity

