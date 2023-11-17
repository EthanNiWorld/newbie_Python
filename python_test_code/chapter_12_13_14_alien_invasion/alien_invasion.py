import sys
import pygame
from setting import Settings #从setting.py中导入Settings类
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()   #创建Clock类的一个实例
        
        self.settings = Settings()  #12.3.4
        """
        #pygame.display.set_mode是控制窗口尺寸的函数，读取setting.py配置
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        """
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        #self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230,230,230)     #12.3.3 设置背景颜色 ，RGB (red,green,blue)
        
        self.ship = Ship(self) #12.4.2 

        self.bullets = pygame.sprite.Group() #存储子弹的组 12.8.3

        self.aliens = pygame.sprite.Group()

        self._create_fleet()    

    def run_game(self):        # 简化主循环
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            """删除已经消失的子弹
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:           #表明飞过屏幕边缘
                    self.bullets.remove(bullet)
            print(len(self.bullets)) """
            self._update_aliens()

            self._update_screen()
            #倾听键盘和鼠标事件
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
            """

            self.clock.tick(60) #设置游戏的帧率
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            ##pygame.KEYDOWN：当用户按下键盘上的任何键时，pygame就会生成一个KEYDOWN事件。这个事件的key属性可以告诉你哪个键被按下。
            elif event.type == pygame.KEYDOWN:      
                self._check_keydown_event(event)
            #pygame.KEYUP：当用户释放键盘上的任何键时，pygame就会生成一个KEYUP事件。这个事件的key属性可以告诉你哪个键被释放。
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
    def _check_keydown_event(self,event):
        """响应按键事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key ==pygame.K_q:     #按Q退出游戏
                sys.exit()
        elif event.key ==pygame.K_SPACE:
            self._fire_bullet()        
    
    def _check_keyup_event(self,event):
        """响应松开事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建子弹，并将其添加到编组bullets中"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 

    def _update_bullets(self):
        """更新子弹的位置"""
        self.bullets.update()
        #删除已经消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)   
        print(len(self.bullets))    
         #检测子弹与飞机的碰撞
        #如果子弹与飞机发生碰撞，就删除子弹，和飞机
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _create_fleet(self):      

        alien = Alien(self)
        alien_width,alien_height = alien.rect.size

        current_x,current_y = alien_width,alien_height

        while current_y < self.settings.screen_height - 3 * alien_height:

            while current_x < self.settings.screen_width - 2 * alien_width:
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width
            current_x = alien_width 
            current_y += 2 * alien_height

    def _create_alien(self,x_position,y_position):
        """创建外星人，并将其添加到编组aliens中"""       
        new_alien = Alien(self)
        new_alien_x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien) 
    
    def _update_aliens(self):

        self.aliens.update()

                
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color) #获取设置中的背景色
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen) #绘制外星人


        pygame.display.flip() #让最近绘制的屏幕可见

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()  