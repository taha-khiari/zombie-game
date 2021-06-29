from palyer import player
from monter import Monster
from comet_event import CometFallEvent
import pygame

class Game:
    def __init__(self):
        self.is_playing= False
        self.all_players = pygame.sprite.Group()
        self.player=player(self)
        self.all_players.add(self.player)
        self.comet_event= CometFallEvent(self)
        self.all_monster = pygame.sprite.Group()

        self.pressed={}
        self.spon_monster()
        self.spon_monster()
    def start(self):
        self.is_playing =True
        self.spon_monster()
        self.spon_monster()

    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):

        screen.blit(self.player.image, self.player.rect)
        self.player.updat_health_bar(screen)
        self.comet_event.update_bar(screen)
        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(screen)

        self.all_monster.draw(screen)

        self.comet_event.all_comet.draw(screen)
        for Monster in self.all_monster:
            Monster.move()
            Monster.updat_health_bar(screen)
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.mouv_R()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.mouv_L()
        for comet in self.comet_event.all_comet:
            comet.fall()

    def check_collision(self, sprite, group):

        return pygame.sprite.spritecollide(sprite, group, False,pygame.sprite.collide_mask)


    def spon_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)