class Settings():
    def __init__(self):
        self.screen_width=320
        self.screen_height=568
        self.plane_speed_factor =3
        self.bullet_speed_factor =5
        self.bullets_allowed =10
        self.enemy_speed_factor=1
        self.enemy_bullet_speed=2
        self.fleet_drop_speed =1
        self.middle_speed =1
        self.hero_life =3
        self.speed_up =1.03
        self.points =5
        self.middle_points=20
        self.score_scale =1.5
        self.min_middle_number =1
        self.min_enemy_number=3
        self.max_enemy_number =8
        self.max_middle_number=5
        self.boss_speed =1
        self.boss_direction =1
        self.init_settings()
    def init_settings(self):
        self.points = 5
        self.enemy_bullet_speed = 2
        self.middle_points = 20
        self.enemy_speed_factor = 1
        self.fleet_drop_speed = 1
        self.plane_speed_factor = 3
        self.bullet_speed_factor = 5
        self.min_middle_number = 1
        self.min_enemy_number=3
        self.hero_life = 3
    def speed_ups(self):
        self.enemy_speed_factor *=self.speed_up
        self.fleet_drop_speed *=self.speed_up
        self.plane_speed_factor *=self.speed_up
        self.bullet_speed_factor *=self.speed_up
        self.enemy_bullet_speed*=self.speed_up