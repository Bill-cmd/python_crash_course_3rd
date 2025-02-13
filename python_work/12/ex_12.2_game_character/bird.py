import pygame

class Bird:
    """管理鸟的类"""

    def __init__(self, bird_game):
        """初始化鸟的属性"""

        self.screen = bird_game.screen
        self.screen_rect = bird_game.screen.get_rect()

        # 加载鸟的图像，并获取其外接矩形
        self.image = pygame.image.load('images/bird.bmp')
        self.rect = self.image.get_rect()

        # 将鸟放在屏幕中央
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """在屏幕上绘制鸟"""
        self.screen.blit(self.image, self.rect)
