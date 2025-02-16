import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和鼠标事件
            self._check_events()
            self.ship.update()
            self._update_bullets() 
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_envents(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            # 停止向右移动飞船
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # 停止向左移动飞船
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入到编组 bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """更新子弹的位置，并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()

        # 删除已消失的子弹
        """
        这里使用了 self.bullets.copy()，这是因为当我们在遍历一个容器时，如果直接修改容器的大小（比如删除元素），
        可能会导致迭代器失效或出现意外行为。为了避免这种情况，代码通过 self.bullets.copy() 创建了一个副本，
        然后在副本上进行遍历，同时安全地修改原始容器
        """
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人, 再不断添加，直到一行放不下为止
        # 外星人的间距为外星人的宽度和外星人的高度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_aliens(current_x, current_y)
                current_x += 2 * alien_width
            # 添加一行外星人后，将 current_x 重置为 alien_width，并在 current_y 下方添加一行外星人
            current_x = alien_width
            current_y += 2 * alien_height
        

    def _create_aliens(self, x_position, y_position):
        """创建一个外星人并放在当前行"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 重绘飞船
        self.ship.blitme()
        # self.aliens.draw(self.screen) 会遍历 self.aliens 中的每个外星人精灵（Alien 对象），
        # 并调用它们的 blitme() 方法（或类似的绘制方法），将它们绘制到 self.screen 上。
        self.aliens.draw(self.screen)

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
