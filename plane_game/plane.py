import pygame
from pygame.sprite import Sprite
class Plane(Sprite):
    def __init__(self,ai_settings,screen):
        super(Plane,self).__init__()
        self.screen =screen
        self.ai_settings =ai_settings
        self.image =pygame.image.load("images\\hero_plane_1.png")
        self.image1=pygame.image.load("images\\hero_plane_1.png")
        self.image2 = pygame.image.load("images\\hero_plane_2.png")
        self.frequency=0
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #在飞船的属性center中存储小数
        self.center =float(self.rect.centerx)
        self.align =float(self.rect.bottom)
        self.moving_right =False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def set_image(self,_image):
        self.image=_image
    def blit_myplane(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.plane_speed_factor
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.center-=self.ai_settings.plane_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.align +=self.ai_settings.plane_speed_factor
        if self.moving_up and self.rect.bottom>80:
            self.align -= self.ai_settings.plane_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom =self.align
        if self.frequency<20:
            self.frequency+=1
            if(self.frequency<10):
                self.image=self.image1
            else:
                self.image=self.image2
        else :
            self.frequency=0

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.align = self.screen_rect.bottom


