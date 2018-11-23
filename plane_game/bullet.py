import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,plane):
        super().__init__()
        self.screen =screen
        self.image = pygame.image.load("images//bullet1.png")
        self.rect =pygame.Rect(0,0,self.image.get_rect().centerx,self.image.get_rect().bottom )
        self.rect.centerx =plane.rect.centerx
        self.rect.top =plane.rect.top
        self.y=float(self.rect.y)
        self.speed_factor =ai_settings.bullet_speed_factor
    def update(self):
        self.y-=float(self.speed_factor)
        self.rect.y =self.y
    def draw_bullet(self):
        #pygame.draw.rect(self.screen,self.color,self.rect)
        self.screen.blit(self.image,self.rect)