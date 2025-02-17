import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """表示单个雨滴的类"""

    def __init__(self, raindrop_game):
        """初始化雨滴并设置其初始位置"""
        super().__init__()
        self.screen = raindrop_game.screen
        self.settings = raindrop_game.settings
        #self.screen_rect = self.screen.get_rect()

        # 加载雨滴图像并获取其外接矩形
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # 每个雨滴最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y =self.rect.height

        # 存储雨滴的准确位置
        #self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制雨滴"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果雨滴到达屏幕边缘，就返回True"""
        self.screen_rect = self.screen.get_rect()
        if self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self):
        """向下移动雨滴"""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
