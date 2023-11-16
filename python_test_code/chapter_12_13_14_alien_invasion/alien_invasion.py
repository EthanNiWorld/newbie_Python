import sys
import pygame
from setting import Settings #从setting.py中导入Settings类
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()   #创建Clock类的一个实例
        
        self.settings = Settings()  #12.3.4
        #pygame.display.set_mode是控制窗口尺寸的函数
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )

        #self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230,230,230)     #12.3.3 设置背景颜色 ，RGB (red,green,blue)
        
        self.ship = Ship(self) #12.4.2 

    def run_game(self):
        """开始游戏主循环"""
        while True:
            #倾听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
            
            #self.screen.fill(self.bg_color) #每次循环都重新绘制屏幕
            self.screen.fill(self.settings.bg_color) #获取设置中的背景色

            self.ship.blitme()

            pygame.display.flip() #让最近绘制的屏幕可见
            self.clock.tick(60) #设置游戏的帧率
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()  