import pygame
import sys
from random import randint
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

        self._create_stars()


    def run_game(self):
        """游戏主循环"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            pygame.display.flip()

    def _get_star_offset(self):
        """获取星星的偏移量"""
        offset_size = 15
        return randint(-1*offset_size, offset_size)

    def _create_star(self, x_postion, y_position):
        """创建一个星星并将其放在屏幕上"""
        new_star = Star(self)
        new_star.rect.x = x_postion + self._get_star_offset()
        new_star.rect.y = y_position + self._get_star_offset()
        self.stars.add(new_star)
        
        
    def _create_stars(self):
        """创建多行星星"""
        # 创建一个星星对象
        star = Star(self)
        # 获取星星的宽度和高度
        star_width, star_height = star.rect.size

        # 初始化当前x和y坐标
        current_x, current_y = 2*star_width, 2*star_height
        # 当当前y坐标小于屏幕高度减去3个星星高度时，循环
        while current_y < (self.settings.screen_height - 3 * star_height):
            # 当当前x坐标小于屏幕宽度减去2个星星宽度时，循环
            while current_x < (self.settings.screen_width - 2 * star_width):
                # 在当前x和y坐标处创建一个星星
                self._create_star(current_x, current_y)
                # 当前x坐标增加2个星星宽度
                current_x += 2*star_width
            # 重置当前x坐标为2个星星宽度
            current_x = 2*star_width
            # 当前y坐标增加2个星星高度
            current_y += 2*star_height
   

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


    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    sg = StarsGame()
    sg.run_game()

