import pygame

class rocket:
    """火箭的设置"""
    def __init__(self, rocket_game):
        """初始化火箭并设置其初始位置"""
        self.screen = rocket_game.screen
        self.screen_rect = rocket_game.screen.get_rect()
        self.settings = rocket_game.settings

        # 加载火箭图像并获取其外接矩形
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        # 在火箭的属性x中存储一个浮点数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整火箭的位置"""
        # 更新火箭的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image, self.rect)
