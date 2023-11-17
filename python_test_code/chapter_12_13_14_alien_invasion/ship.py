import pygame

class Ship:
    """管理飞船"""
    def __init__(self,ai_game):
        """初始化飞船并设置初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #把所有游戏元素当作矩形处理

        #
        self.image = pygame.image.load('/Users/ethan/Downloads/WechatIMG3370.jpg')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom   


        self.x = float(self.rect.x) #存储浮点数

        #移动标志 （一开始不移动）  12.6.2
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """根据移动标志更新飞船的位置"""
        
        #更新飞船属性x值
        if self.moving_right and self.rect.right < self.screen_rect.right:      #如果右移,且飞船没有到达右边界
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: #如果左移
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x    

    def blitme(self):
        #在指定的位置绘制飞船
        self.screen.blit(self.image,self.rect)