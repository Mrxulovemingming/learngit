import pygame
from pygame.sprite import Sprite
from enemy_bullet import Enemy_bullet
class Boss(Sprite):
    def __init__(self,ai_settings,screen):
        super(Boss,self).__init__()
        self.screen =screen
        self.ai_settings =ai_settings
        self.image=pygame.image.load("images//enemy2_fly_1.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x =float(self.rect.x)
        self.direction =1
        self.life =10
        self.move=1
        self.bullets = pygame.sprite.Group()
        self.attak_frequency=1
    def shoot(self):
        bullet =Enemy_bullet(self.ai_settings,self.screen,self)
        self.bullets.add(bullet)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.move%2==0:
            self.rect.x-=(self.ai_settings.boss_speed*self.direction)
            self.check_edge()
        if(self.attak_frequency%100==0):
            self.shoot()
        self.move+=1
        self.attak_frequency+=1
        self.fire()
    def fire(self):
        self.bullets.draw(self.screen)
        self.bullets.update()
    def change_direction(self):
        self.direction*=-1
    def check_edge(self):
        if self.rect.x <=0:
            self.change_direction()
        if self.rect.x>=self.screen.get_rect().width -self.rect.width:
            self.change_direction()
