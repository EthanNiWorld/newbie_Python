import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """单个外星人的类"""
    
    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #加载外星人图片
        self.image = pygame.image.load('/Users/ethan/Downloads/hf_logo.png')
        self.rect = self.image.get_rect()
        # Start each new alien at the center of the screen.
        self.rect.x = self.screen.get_rect().centerx
        self.rect.y = self.screen.get_rect().centery - 500
        #存储外星人的水平位置
        self.x = float(self.rect.x)
    
    def check_edge(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)


    def update(self):
        #更新外星人的位置
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        #更新外星人的位置
        self.rect.x = self.x