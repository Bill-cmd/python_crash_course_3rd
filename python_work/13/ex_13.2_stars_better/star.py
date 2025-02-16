import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """表示单个星星的类"""

    def __init__(self, stars_game):
        """初始化星星并设置其初始位置"""
        super().__init__()
        self.screen = stars_game.screen
        #self.screen_rect = self.screen.get_rect()

        # 加载星星图像并获取其外接矩形
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # 每个星星最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y =self.rect.height

        # 存储星星的准确位置
        #self.x = float(self.rect.x)
        #self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)

