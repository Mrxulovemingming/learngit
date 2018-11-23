import pygame
from pygame.sprite import Sprite
class Mysprite(Sprite):
    def __init__(self,target):
        pygame.sprite.Sprite.__init__(self)
        #用来存储展示图片用的界面,如screen
        self.target_surface =target
        self.image =None
        self.master_image=None
        self.rect =None
        self.topleft =0,0
        self.frame =0
        self.old_frame=-1
        self.frame_width=1
        self.frame_height=1
        self.first_frame =0
        self.last_frame=0
        self.columns =1
        self.last_time =0

    def load(self,filename,width,height,columns):
        #convert_alpha()使用透明的方法绘制前景图像
        self.master_image =pygame.image.load(filename).convert_alpha()
        self.frame_width =width
        self.frame_height =height
        self.rect=0,0,width,height
        self.columns=columns
        #master_image即传入的那张序列图
        rect =self.master_image.get_rect()
        #获取序列图中最后一张的下标，因为下标从0开始，所以最后减一
        self.last_frame=(rect.width//width)*(rect.height//height)-1
    def update(self, current_time,rate =200):
        if current_time>self.last_time+rate:
            self.frame+=1
            if self.frame>self.last_frame:
                self.frame=self.first_frame
            self.last_time =current_time
        if self.frame!=self.old_frame:
            frame_x =(self.frame%self.columns)*self.frame_width
            frame_y =(self.frame//self.columns)*self.frame_height
            rect=(frame_x,frame_y,self.frame_width,self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame=self.frame
# pygame.init()
# screen = pygame.display.set_mode((200,300))
# pygame.display.set_caption("精灵类测试")
# framerate =pygame.time.Clock()
# cat = Mysprite(screen)
# cat.load("images//boss_broken_procdure.png",110,169,6)
# group =pygame.sprite.Group()
# group.add(cat)
# while True:
#     framerate.tick(30)
#     ticks =pygame.time.get_ticks()
#     for event in pygame.event.get():
#         if event.type ==pygame.QUIT:
#             pygame.quit()
#             exit()
#     key = pygame.key.get_pressed()
#     if key[pygame.K_SPACE]:
#         exit()
#     screen.fill((0,0,100))
#     group.update(ticks)
#     group.draw(screen)
#     pygame.display.update()