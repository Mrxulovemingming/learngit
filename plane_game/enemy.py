import pygame
from pygame.sprite import Sprite
class Enemy(Sprite):
    def __init__(self,ai_settings,screen):
        super(Enemy,self).__init__()
        self.screen =screen
        self.ai_settings =ai_settings
        self.image=pygame.image.load("images//enemy1_fly_1.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x =float(self.rect.x)
        self.life =0
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.rect.y+=self.ai_settings.fleet_drop_speed