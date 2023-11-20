import pygame.font #导入字体库

class Button():
    def __init__(self,ai_game,msg):
        # 1.设置按钮的属性
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 2.设置按钮的位置
        self.width,self.height = 300,50
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        #创建按钮的ract对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)


    def _prep_msg(self,msg):
        """将msg渲染为图像，并使其居中"""
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color) #font.render将msg渲染为图像
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """绘制按钮"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

        """实际上，_prep_msg和draw_button会生成两个矩形，一个是按钮的矩形，一个是按钮上的文本的矩形"""