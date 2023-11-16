import pygame

class Ship:
    """管理飞船"""
    def __init__(self,ai_game):
        """初始化飞船并设置初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() #把所有游戏元素当作矩形处理

        #
        self.image = pygame.image.load('/Users/ethan/Downloads/WechatIMG3370.jpg')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        #在指定的位置绘制飞船
        self.screen.blit(self.image,self.rect)