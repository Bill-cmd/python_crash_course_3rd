import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # 窗口模式
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        """
        # 全屏模式
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # 设置背景颜色
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和鼠标事件
            self._check_events()
            self.ship.update()
            # 每次循环时都重绘屏幕
            self._update_screen()
            # 控制游戏刷新速度
            self.clock.tick(60)
    

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_envents(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_envents(event)


    def _check_keydown_envents(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_envents(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            # 停止向右移动飞船
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # 停止向左移动飞船
            self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 重绘飞船
        self.ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
