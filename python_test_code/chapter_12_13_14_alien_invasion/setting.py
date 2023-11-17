class Settings:
    """存储游戏中所有的设置"""
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.ship_speed = 1.5  #设置飞船速度 ，1.5像素
        self.bullet_speed = 3


        #子弹设置
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60  #灰色
        self.bullets_allowed = 20

        #外星人设置
        self.alien_speed = 0.8
            
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  #1向右  -1向左
