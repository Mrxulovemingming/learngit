#用于纪录游戏的状态
class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings =ai_settings
        self.reset_stats()
        self.game_active =False
        self.game_state =False
        self.score =0
        self.level =1
        self.kill_middle=0
        self.kill_enemy=0
        self.boss_state=False
    def reset_stats(self):
        self.hero_left =self.ai_settings.hero_life