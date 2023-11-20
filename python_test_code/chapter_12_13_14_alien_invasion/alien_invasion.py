import sys
from time import sleep
import pygame
from setting import Settings #从setting.py中导入Settings类
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard


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
        #创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)  #创建记分牌

        self.ship = Ship(self) #12.4.2 

        self.bullets = pygame.sprite.Group() #存储子弹的组 12.8.3

        self.aliens = pygame.sprite.Group()

        self._create_fleet()   

        self.game_active = False  #游戏启动后属于非活跃状态

        self.play_button = Button(self,"Play, Mr Ethan")

    def run_game(self):        # 简化主循环
        """开始游戏主循环"""
        while True:
            self._check_events()

            if self.game_active:
               
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            """删除已经消失的子弹
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:           #表明飞过屏幕边缘
                    self.bullets.remove(bullet)
            print(len(self.bullets)) """
                

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # 获取鼠标的位置(x,y)
                self._check_play_button(mouse_pos) 

     
    def _check_play_button(self,mouse_pos):
        """响应按键"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active: # 判断鼠标是否点击了按钮
            self.settings.initial_dynamic_settings()
            self.stats.reset_stats()
            self.game_active = True

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship() 
            #隐藏鼠标的光标
            pygame.mouse.set_visible(False)       

                            
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
        #print(len(self.bullets))    
         #检测子弹与飞机的碰撞
        #如果子弹与飞机发生碰撞，就删除子弹，和飞机
        self._check_bullet_alien_collisions()



    def _check_bullet_alien_collisions(self):
        #检测子弹与飞机的碰撞
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            self.stats.score += self.settings.alien_points
            print("update score")
            self.sb.prep_score()
        
        if not self.aliens:#如果飞机被摧毁，就创建一个新 fleet
            #删除现有子弹，并创建一个新的舰队
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed() 

    
    def _create_fleet(self):      

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size #外星人的间距是外星人的宽带和高度

        current_x, current_y = alien_width,alien_height

        while current_y < (self.settings.screen_height - 5 * alien_height):

            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 1.5 * alien_width

            current_x = alien_width 
            current_y += 3 * alien_height
            
    """CHATGPT生成
    def _create_fleet(self): 
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size  # Width and height of each alien

        # Set the spacing between aliens
        horizontal_spacing = 1.2 * alien_width
        vertical_spacing = 1.2 * alien_height

        # Calculate the number of columns and rows based on available space
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_columns = int(available_space_x / horizontal_spacing)

        available_space_y = self.settings.screen_height - 3 * alien_height - self.ship.rect.height
        number_rows = int(available_space_y / vertical_spacing)

        for row_number in range(number_rows):
            for column_number in range(number_columns):
                x_position = column_number * horizontal_spacing
                y_position = row_number * vertical_spacing
                self._create_alien(x_position, y_position)"""

    def _check_fleet_edges(self):
        #当外星人到达边缘时，改变方向
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        #将整个外星舰队向下移动，并改变他们的方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, x_position, y_position):
        """创建外星人,并将其添加到编组aliens中      
        new_alien = Alien(self)
        new_alien_x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien) """ 

        alien = Alien(self)
        #alien_width, alien_height = alien.rect.size
        alien.x = x_position
        alien.rect.x = x_position
        alien.rect.y = y_position
        self.aliens.add(alien)
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Shi hit")
            self._ship_hit()
        
        self._check_aliens_bottom()
    def _check_aliens_bottom(self):
        #检查是否有外星人到达屏幕底部 
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break    

    def _ship_hit(self):
        if self.stats.ships_left >0:
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)

        else:
            self.game_active = False
            print("You lost all your ships")
            pygame.mouse.set_visible(True) #重新显示光标


                
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color) #获取设置中的背景色
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen) #绘制外星人
        self.sb.show_score()


        if not self.game_active:
            self.play_button.draw_button()


        pygame.display.flip() #让最近绘制的屏幕可见

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()  