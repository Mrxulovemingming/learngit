import pygame.ftfont
from pygame.sprite import Group
from plane import  Plane
class Score():
    def __init__(self,ai_settings,screen,stats):
        self.screen =screen
        self.ai_settings =ai_settings
        self.screen_rect =screen.get_rect()
        self.stats = stats
        self.text_color=(30,30,30)
        #字体设置
        self.font = pygame.font.SysFont(None,28)
        self.init_score()
        self.init_level()
        self.init_left_life()
    def init_left_life(self):
        self.planes = Group()
        for life in range(self.stats.hero_left):
            plane = Plane(self.ai_settings,self.screen)
            plane.rect.x =10 +life*40
            plane.rect.y=10
            _image = pygame.image.load("images\\hero_plane_1.png")
            heart =pygame.transform.scale(_image,(40,40))
            plane.set_image(heart)
            self.planes.add(plane)
    def init_level(self):
        level_str = str(self.stats.level)
        # 第二个布尔值参数这是否开启抗锯齿
        self.level_image = self.font.render(level_str, True, self.text_color, self)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 43
    def init_score(self):
        score_str = str(self.stats.score)
        #第二个布尔值参数这是否开启抗锯齿
        self.score_image = self.font.render(score_str,True,self.text_color,self)
        self.score_rect =self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right-20
        self.score_rect.top =20
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.planes.draw(self.screen)
    def reset_score(self):
        self.stats.score=0
    def reset_level(self):
        self.stats.level=1

