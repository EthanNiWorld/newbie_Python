class Settings:
    """存储游戏中所有的设置"""
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #飞船设置
        self.ship_speed = 3  #设置飞船速度 ，1.5像素
        self.ship_limit = 3
        self.bullet_speed = 5


        #子弹设置
        self.bullet_speed = 3.0
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = 60,60,60  #灰色
        self.bullets_allowed = 20

        #外星人设置
        self.alien_speed = 3
        self.speedup_scale = 1.1   #以什么速度加快游戏节奏
        self.initial_dynamic_settings()
            
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  #1向右  -1向左

    def initial_dynamic_settings(self):
        """初始化外星人和子弹的动态设置"""
        self.alien_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0


        self.fleet_direction = 1

        self.alien_points = 5


    def increase_speed(self):
        """提高速度"""
        self.alien_speed += self.speedup_scale
        self.bullet_speed += self.speedup_scale
        self.ship_speed += self.speedup_scale  



     
