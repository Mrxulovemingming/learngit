import pygame
from  settings import Settings
from plane import Plane
import game_functions as gf
from pygame.sprite import Group
from  game_stats import GameStats
from mysprite import Mysprite
from button import Button
from  score import  Score
import random
def run_game():
    pygame.init()
    ai_settings =Settings()
    #pygame.display.set_mode返回一个surface对象
    screen =pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    bullet_sound = pygame.mixer.Sound('sound/bullet.wav')
    bullet_sound.set_volume(0.3)
    pygame.mixer.music.load('sound/game_music.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)
    enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
    enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
    enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
    game_over_sound = pygame.mixer.Sound('sound/game_over.wav')
    enemy1_down_sound.set_volume(0.3)
    enemy2_down_sound.set_volume(0.4)
    enemy3_down_sound.set_volume(0.5)
    game_over_sound.set_volume(0.3)
    shoot_frequency = 0
    enemy_frequency =0
    background =pygame.image.load("images\\background_1.png").convert()
    _game_over = pygame.image.load('images/gameover.png')
    game_over =pygame.transform.scale(_game_over,(320,568))
    pygame.display.set_caption("plane_war")
    play_button =Button(ai_settings,screen,"play")
    stats =GameStats(ai_settings)
    s = Score(ai_settings,screen,stats)
    plane = Plane(ai_settings,screen)
    bullets = Group()
    framerate = pygame.time.Clock()
    Heroplane = Mysprite(screen)
    Heroplane.load("images//hero_plane_1.png", 66, 80, 2)
    group =pygame.sprite.Group()
    group.add(Heroplane)
    enemys =Group()
    middle =Group()
    middle_frequency=0
    enemies_down = pygame.sprite.Group()
    breakplane =Group()
    middle_down =pygame.sprite.Group()
    bosses = Group()
    break_boss =Group()
    delay = 0
    delay_1 =0
    delay_2=0
    delay_3 =0
    while True:
        framerate.tick(60)
        #blit用于在screen上绘制图像
        screen.blit(background, (0, 0))
        gf.check_events(ai_settings,screen,stats,play_button,plane,enemys,bullets,bullet_sound,s)
        if stats.game_active and not stats.boss_state:
            plane.update()
            middle.update()
            gf.update_bullets(ai_settings,screen,plane,enemys,bullets,stats,s,shoot_frequency,enemies_down,enemy1_down_sound,middle,middle_down,enemy2_down_sound,bosses,break_boss,enemy3_down_sound)
            gf.update_enemys(ai_settings,stats,screen,plane,enemys,bullets,s,play_button,breakplane,game_over_sound,enemies_down,middle,middle_down,bosses)
            if enemy_frequency % 60 == 0 and len(enemys) < ai_settings.min_enemy_number:
                gf.create_fleet(ai_settings, screen, plane, enemys)
            else:
                enemy_frequency += 1
            if middle_frequency%100 ==0 and len(middle)<ai_settings.min_middle_number:
                gf.create_middle_enemys(ai_settings,screen,middle)
            else:
                middle_frequency+=1
        if stats.game_active and  stats.boss_state:
            plane.update()
            gf.update_bullets(ai_settings, screen, plane, enemys, bullets, stats, s, shoot_frequency, enemies_down,
                              enemy1_down_sound, middle, middle_down, enemy2_down_sound,bosses,break_boss,enemy3_down_sound)
            gf.update_bosses(ai_settings,plane,breakplane,stats,s,game_over_sound,play_button,bosses)
            if(len(bosses)<=0):
                gf.create_boss(ai_settings,screen,bosses)
            bosses.update()
        if not stats.game_active and  stats.game_state:
            enemys.empty()
            bullets.empty()
            screen.blit(game_over,(0,0))
        for planes in breakplane:
            if delay<10:
                planes.image=pygame.image.load("images\\hero_break1.png")
                delay+=1
            elif delay<20:
                planes.image = pygame.image.load("images\\hero_break2.png")
                delay += 1
            elif delay<30:
                planes.image = pygame.image.load("images\\hero_break3.png")
                delay += 1
            elif delay<40:
                planes.image = pygame.image.load("images\\hero_break4.png")
                delay += 1
            screen.blit(planes.image, plane.rect)
            if delay >= 40:
                delay = 0
                breakplane.remove(plane)
        for enemy_down in enemies_down:
            if delay_1<10:
                enemy_down.image=pygame.image.load("images\\enemy1_1.png")
                delay_1+=1
            elif delay_1<20:
                enemy_down.image = pygame.image.load("images\\enemy1_2.png")
                delay_1 += 1
            elif delay_1<30:
                enemy_down.image = pygame.image.load("images\\enemy1_3.png")
                delay_1 += 1
            elif delay_1<40:
                enemy_down.image = pygame.image.load("images\\enemy1_4.png")
                delay_1 += 1

            screen.blit(enemy_down.image, enemy_down.rect)
            if delay_1>=40:
                delay_1 =0
                enemies_down.remove(enemy_down)
        for mi_down in middle_down:
            if delay_2<10:
                mi_down.image=pygame.image.load("images\\middle_1.png")
                delay_2+=1
            elif delay_2<20:
                mi_down.image = pygame.image.load("images\\middle_2.png")
                delay_2 += 1
            elif delay_2<30:
                mi_down.image = pygame.image.load("images\\middle_3.png")
                delay_2 += 1
            elif delay_2<40:
                mi_down.image = pygame.image.load("images\\middle_4.png")
                delay_2 += 1

            screen.blit(mi_down.image, mi_down.rect)
            if delay_2>=40:
                delay_2 =0
                middle_down.remove(mi_down)
        for boss_down in break_boss:
            if delay_3 < 10:
                boss_down.image = pygame.image.load("images\\boss_1.png")
                delay_3 += 1
            elif delay_3 < 20:
                boss_down.image = pygame.image.load("images\\boss_2.png")
                delay_3 += 1
            elif delay_3 < 30:
                boss_down.image = pygame.image.load("images\\boss_3.png")
                delay_3 += 1
            elif delay_3 < 40:
                boss_down.image = pygame.image.load("images\\boss_4.png")
                delay_3 += 1
            elif delay_3 < 50:
                boss_down.image = pygame.image.load("images\\boss_4.png")
                delay_3 += 1
            elif delay_3 < 60:
                boss_down.image = pygame.image.load("images\\boss_4.png")
                delay_3 += 1

            screen.blit(boss_down.image, boss_down.rect)
            if delay_3 >= 60:
                delay_3 = 0
                break_boss.remove(boss_down)
        gf.update_screen(ai_settings,screen,stats,plane,enemys,bullets,play_button,s,middle,bosses)

        pygame.display.update()
run_game()

