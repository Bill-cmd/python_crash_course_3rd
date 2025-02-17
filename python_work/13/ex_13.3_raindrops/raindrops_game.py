import pygame
import sys

from settings import Settings
from raindrop import Raindrop


class RaindropGame:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.raindrops = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")

        self._create_raindrops()


    def run_game(self):
        """游戏主循环"""
        while True:
            self._check_events()
            #self.raindrops.update()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)
            pygame.display.flip()


    def _create_raindrop(self, x_postion, y_position):
        """创建一个雨滴并将其放在屏幕上"""
        new_raindrop = Raindrop(self)
        # 
        new_raindrop.y = y_position
        new_raindrop.rect.x = x_postion
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)
        
        
    def _create_raindrops(self):
        """创建多行雨滴"""
        # 创建一个雨滴对象
        raindrop = Raindrop(self)
        # 获取雨滴的宽度和高度
        raindrop_width, raindrop_height = raindrop.rect.size

        # 初始化当前x和y坐标
        current_x, current_y = 2*raindrop_width, 2*raindrop_height
        # 当当前y坐标小于屏幕高度减去3个雨滴高度时，循环
        while current_y < (self.settings.screen_height - 1 * raindrop_height):
            # 当当前x坐标小于屏幕宽度减去2个雨滴宽度时，循环
            while current_x < (self.settings.screen_width - 2 * raindrop_width):
                # 在当前x和y坐标处创建一个雨滴
                self._create_raindrop(current_x, current_y)
                # 当前x坐标增加2个雨滴宽度
                current_x += 2*raindrop_width
            # 重置当前x坐标为2个雨滴宽度
            current_x = 2*raindrop_width
            # 当前y坐标增加2个雨滴高度
            current_y += 2*raindrop_height
   

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

    def _update_raindrops(self):
        """更新雨滴的位置，并删除消失的雨滴"""
        self.raindrops.update()
        for raindrop in self.raindrops.copy():
            if raindrop.rect.bottom >= self.settings.screen_height:
                self.raindrops.remove(raindrop)
            print(len(self.raindrops))

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    rg = RaindropGame()
    rg.run_game()

