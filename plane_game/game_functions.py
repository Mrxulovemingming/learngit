import  sys
import pygame
from time import sleep
from bullet import  Bullet
from enemy import Enemy
from middle_enemy import Middle_Enemy
from random import randint
from boss import Boss
def get_plane_place(plane):
    plane_place_x =plane.rect.left
    plane_place_y = plane.rect.top
    return plane_place_x,plane_place_y
def create_boss(ai_settings,screen,bosses):
    boss = Boss(ai_settings,screen)
    screen_rect = screen.get_rect()
    boss.rect.x = screen_rect.centerx
    boss.rect.y=0
    boss.shoot()
    bosses.add(boss)

def create_middle_enemys(ai_settings,screen,middle):
    enemy = Middle_Enemy(ai_settings, screen)
    enemy_width = enemy.rect.width
    enemy.x = randint(0, ai_settings.screen_width - enemy_width)
    enemy.rect.x = enemy.x
    enemy.rect.y = 0
    enemy.shoot()
    middle.add(enemy)
def plane_hit(ai_settings,stats,screen,plane,enemys,bullets,scores,playbutton,breakplane,game_over_sound,middle):
    if stats.hero_left>0:
        stats.hero_left -=1
        scores.init_left_life ()
        game_over_sound.play()
    #hero被撞击到时，清空bullets和enemy
        enemys.empty()
        bullets.empty()
        middle.empty()
        create_fleet(ai_settings,screen,plane,enemys)
        # plane.center_ship()
        sleep(0.5)
    else:
        middle.empty()
        scores.reset_score()
        scores.reset_level()
        game_over_sound.play()
        stats.game_active=False
        stats.game_state=True
        pygame.mouse.set_visible(True)
        playbutton.prep_msg("replay")
        scores.init_left_life()
        scores.init_level()
        ai_settings.init_settings()
        scores.init_score()

def get_row_number(ai_settings,plane_height,enemy_height):
    avaiable_space_y =(ai_settings.screen_height-(3*enemy_height)-plane_height)
    row_number =int(avaiable_space_y/(2*enemy_height))
    return row_number
def get_enemy_number_x(ai_settings,enemy_width):
    avaible_space_x = ai_settings.screen_width - 40
    # 一行中能创 建的敌机数量
    number_enemy_x = avaible_space_x // (2 * enemy_width)
    return number_enemy_x
def create_enemy(ai_settings,screen,enemys):
    enemy = Enemy(ai_settings, screen)
    enemy_width =enemy.rect.width
    enemy.x = randint(0,ai_settings.screen_width-enemy_width)
    enemy.rect.x = enemy.x
    enemy.rect.y=0
    enemys.add(enemy)
def create_fleet(ai_settings,screen,plane,enemys):
    create_enemy(ai_settings,screen,enemys)
#检查按下按键时的事件
def check_keydown_events(event,ai_settings,screen,plane,bullets,bullet_sound):
    if event.key == pygame.K_RIGHT:
        plane.moving_right = True
    elif event.key == pygame.K_LEFT:
        plane.moving_left = True
    elif event.key == pygame.K_UP:
        plane.moving_up = True
    elif event.key == pygame.K_DOWN:
        plane.moving_down = True
    elif event.key ==pygame.K_SPACE:
       fire_bullet(ai_settings,screen,plane,bullets,bullet_sound)
    #按下p时退出游戏
    elif event.key ==pygame.K_p:
        sys.exit()
def check_keyup_events(event,plane):
    if event.key == pygame.K_RIGHT:
        plane.moving_right = False
    elif event.key == pygame.K_LEFT:
        plane.moving_left = False
    elif event.key == pygame.K_UP:
        plane.moving_up = False
    elif event.key == pygame.K_DOWN:
        plane.moving_down = False
def check_events(ai_settings,screen,stats,play_button,plane,enemys,bullets,bullet_sound,scores):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,plane,bullets,bullet_sound)
        elif event.type == pygame.KEYUP:
           check_keyup_events(event,plane)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,plane,enemys,bullets,mouse_x,mouse_y,scores)
def check_play_button(ai_settings,screen,stats,play_button,plane,enemys,bullets,mouse_x,mouse_y,scores):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        ai_settings.init_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active=True
        scores.init_left_life()
        scores.init_score()
        enemys.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,plane,enemys)
        plane.center_ship()
def update_screen(ai_settings,screen,stats,plane,enemys,bullets,play_button,score,middle,bosses):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    plane.blit_myplane()
    enemys.draw(screen)
    middle.draw(screen)
    if stats.boss_state:
        bosses.draw(screen)

    for mi in middle:
        screen_rect = screen.get_rect()
        mi.fire()
        for bu in mi.bullets:
            if bu.rect.bottom>=screen_rect.bottom:
                mi.bullets.remove(bu)
        if len(mi.bullets)==0:
            mi.shoot()
    score.show_score()
    if not stats.game_active:
        play_button.draw_button()
def update_bullets(ai_settings,screen,plane,enemys,bullets,stats,scores,shoot_frequency,
                   enemies_down,enemy1_down_sound,middle,middle_down,enemy2_down_sound,bosses,break_boss,boss_sound):
    bullets.update()
    for bullet in bullets:
        for boss in bosses:
            if pygame.sprite.collide_circle(boss,bullet):
                bullets.remove(bullet)
                if boss.life > 0:
                    boss.life -= 1
                    if boss.life<=20:
                        boss.image=pygame.image.load("images\\boss_hurt.png")
                else:
                    boss_sound.play()
                    break_boss.add(boss)
                    bosses.remove(boss)
                    stats.boss_state=False
                    stats.kill_enemy+=1
                    enemy1_down_sound.play()
                    stats.kill_enemy += 1
                    stats.score += ai_settings.points
                    scores.init_score()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #collisions是一个字典，键是bullets，值是enemys
    # collisions =pygame.sprite.groupcollide(bullets,enemys,True,True)
    # if(collisions):
    #     for enemys in collisions.values():
    #         stats.score +=ai_settings.points*len(enemys)
    #         scores.init_score()
    for enemy in enemys:
        for bullet in bullets:
            if pygame.sprite.collide_circle(enemy, bullet):
                bullets.remove(bullet)
                if enemy.life>0:
                    enemy.life-=1
                else:
                    enemy1_down_sound.play()
                    stats.kill_enemy+=1
                    enemies_down.add(enemy)
                    enemys.remove(enemy)
                    stats.score += ai_settings.points
                    scores.init_score()
    for mi in middle:
        for bullet in bullets:
            if pygame.sprite.collide_circle(mi,bullet):
                bullets.remove(bullet)
                if mi.life>0:
                    mi.life-=1
                    mi.image=pygame.image.load("images//middle_hurt.png").convert_alpha()
                else:
                    enemy2_down_sound.play()
                    stats.kill_middle+=1
                    middle_down.add(mi)
                    middle.remove(mi)
                    stats.score += ai_settings.middle_points
                    scores.init_score()
    if stats.kill_middle %5==0 and stats.kill_middle>0:
        stats.kill_middle+=1
        if ai_settings.min_middle_number < ai_settings.max_middle_number:
            ai_settings.min_middle_number+=1
        stats.level += 1
        scores.init_level()
    if stats.kill_enemy %9==0 and stats.kill_enemy>0:
        stats.kill_enemy+=1
        if ai_settings.min_enemy_number<ai_settings.max_enemy_number:
            ai_settings.min_enemy_number += 1
        ai_settings.speed_ups()
        stats.level+=1
        scores.init_level()
        ai_settings.points=int(ai_settings.score_scale*ai_settings.points)
        ai_settings.middle_points = int(ai_settings.score_scale * ai_settings.middle_points)
    if stats.kill_enemy%50==0 and stats.kill_enemy>0 :
        stats.boss_state=True
        middle.empty()
        enemys.empty()

def fire_bullet(ai_settings,screen,plane,bullets,bullet_sound):
    # 创建一颗子弹,并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, plane)
        bullets.add(new_bullet)
        bullet_sound.play()
def check_enemys_bottom(ai_settings,stats,screen,plane,enemys,bullets,scores,playbutton):
    screen_rect = screen.get_rect()
    for enemy in enemys.sprites():
        if enemy.rect.bottom>=screen_rect.bottom:
            enemys.remove(enemy)
def check_middle_bottom(screen,middle):
    screen_rect = screen.get_rect()
    for enemy in middle.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            middle.remove(enemy)
def plane_attacked(ai_settings,plane,breakplane,stats,scores,game_over_sound,playbutton,bosses):
    if stats.hero_left > 0:
        stats.hero_left -= 1
        for boss in bosses:
            boss.bullets.empty()
        scores.init_left_life()
        game_over_sound.play()
    else:
        bosses.empty()
        scores.reset_score()
        scores.reset_level()
        game_over_sound.play()
        stats.game_active = False
        stats.game_state = True
        stats.boss_state =False
        pygame.mouse.set_visible(True)
        playbutton.prep_msg("replay")
        scores.init_left_life()
        scores.init_level()
        ai_settings.init_settings()
        scores.init_score()
def update_bosses(ai_settings,plane,breakplane,stats,scores,game_over_sound,playbutton,bosses):
    bosses.update()
    for boss in bosses:
        for bu in boss.bullets:
            if pygame.sprite.collide_circle(bu, plane):
                breakplane.add(plane)
                plane_attacked(ai_settings, plane, breakplane, stats, scores, game_over_sound, playbutton,bosses)
def update_enemys(ai_settings,stats,screen,plane,enemys,bullets,scores,playbutton,breakplane,game_over_sound,enemies_down,middle,middle_down,bosses):
    # check_fleet_edges(ai_settings,enemys)
    enemys.update()
    for enemy in enemys:
        if pygame.sprite.collide_circle(enemy, plane):
            enemies_down.add(enemy)
            breakplane.add(plane)
            plane_hit(ai_settings,stats,screen,plane,enemys,bullets,scores,playbutton,breakplane,game_over_sound,middle)
        for mi in middle:
            if pygame.sprite.collide_circle(mi, plane):
                middle_down.add(mi)
                breakplane.add(plane)
                plane_hit(ai_settings, stats, screen, plane, enemys, bullets, scores, playbutton, breakplane,
                          game_over_sound, middle)
            for bu in mi.bullets:
                if pygame.sprite.collide_circle(bu,plane):
                    breakplane.add(plane)
                    plane_hit(ai_settings, stats, screen, plane, enemys, bullets, scores, playbutton, breakplane,
                              game_over_sound, middle)

    check_enemys_bottom(ai_settings,stats,screen,plane,enemys,bullets,scores,playbutton)
    check_middle_bottom(screen,middle)
