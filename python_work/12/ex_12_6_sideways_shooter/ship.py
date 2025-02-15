import pygame

class Ship:
    """表示飞船的类"""
    def __init__(self, ship_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ship_game.screen
        self.screen_rect = ship_game.screen.get_rect()
        self.settings = ship_game.settings

        # 加载  飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()

        # 将每艘飞船放在屏幕左侧中央
        self.rect.midleft = self.screen_rect.midleft

        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y    


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)



    