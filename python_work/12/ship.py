import pygame
from settings import Settings

class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储一个浮点数
        self.x = float(self.rect.x)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
    

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的属性x值，而不是其外接矩形的属性x的值
        if self.moving_right:
            self.x += self.settings.ship_speed

        if self.moving_left:
            self.x -= self.settings.ship_speed

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


        
        
