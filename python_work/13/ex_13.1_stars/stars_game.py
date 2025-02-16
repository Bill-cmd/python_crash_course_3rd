import pygame
import sys

from settings import Settings
from star import Star


class StarsGame:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.stars = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")

        self._create_star()

    def run_game(self):
        """游戏主循环"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

    def _create_star(self):
        """创建一行星星并将其放在屏幕上"""
        star = Star(self)
        star_width, star_height = star.rect.size
        
        current_x, current_y = 2*star_width, 2*star_height

        

        self.stars.add(star)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_q:
            sys.exit()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    sg = StarsGame()
    sg.run_game()

