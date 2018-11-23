import pygame
from pygame.sprite import Sprite
from enemy_bullet import Enemy_bullet
class Middle_Enemy(Sprite):
    def __init__(self,ai_settings,screen):
        super(Middle_Enemy,self).__init__()
        self.screen =screen
        self.ai_settings =ai_settings
        self.image=pygame.image.load("images//enemy3_fly_1.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x =float(self.rect.x)
        self.life =3
        self.bullet_allowed =3
        self.bullets = pygame.sprite.Group()
    def shoot(self):
        bullet =Enemy_bullet(self.ai_settings,self.screen,self)
        self.bullets.add(bullet)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.rect.y+=self.ai_settings.middle_speed
    def fire(self):
        self.bullets.draw(self.screen)
        self.bullets.update()