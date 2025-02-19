import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        """
        # 全屏模式
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """
        # 窗口模式
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        # 创建一个用于存储游戏统计信息的实例
        self.sb = Scoreboard(self)

        # 创建飞船
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # 创建外星舰队
        self._create_fleet()

        # 游戏启动后处于活动状态
        self.game_active = False

        #创建Play按钮
        self.play_button = Button(self, "Play")

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和鼠标事件
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets() 
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # pygame.mouse.get_pos()，它返回⼀个元组，其中包含玩家单击⿏标时光标的 x 坐标和 y 坐标
                mouse_pos = pygame.mouse.get_pos()
                # 将这个元组传递给新⽅法 _check_play_button()，看看玩家是否单击了按钮
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """在玩家单击Play按钮时开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # 还原游戏难度
            self.settings.initialize_dynamic_settings()
            # 重置游戏统计信息
            self.stats.reset_stats()
            # 重置游戏得分
            self.sb.prep_score()
            # 重置等级
            self.sb.prep_level()
            # 清空外星人列表和子弹列表
            self.aliens.empty()
            self.bullets.empty()
            # 创建新的外星人群，并让飞船居中
            self._create_fleet()
            self.ship.center_ship()
            # 隐藏光标
            pygame.mouse.set_visible(False)
            # 重置游戏活动标志
            self.game_active = True


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
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人的碰撞"""
        # 检查是否有子弹击中了外星人
        # 如果是这样，就删除相应的子弹和外星人
        # 将 self.bullets 中的所有⼦弹与 self.aliens 中的所有外星⼈进⾏⽐较，看它们是否重叠了在⼀起。每当有⼦弹和外星⼈的rect 重叠时，
        # groupcollide() 就在返回的字典中添加⼀个键值对。两个值为 True 的实参告诉 Pygame 在发⽣碰撞时删除对应的⼦弹和外星⼈
        # 高能子弹：子弹击中外星人后，外星人消失，子弹不消失，第一个实参为False，第二个实参为True
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            # 如果字典 collisions 存在，就遍历其中的所有值。每个值都是⼀个列表，包含被同⼀颗⼦弹击中的所有外星⼈。
            # 对于每个列表，都将其包含的外星⼈数量乘以⼀个外星⼈的分数，并将结果加⼊当前得分
            for aliiens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliiens)
            #self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            # 检查更新最高分
            self.sb.check_high_score()

        # 整个外星舰队被全部击落后执行的任务(游戏难度升级并提高等级)
        if not self.aliens:
            # 删除现有的子弹并创建新的外星人群
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # 提高等级
            self.stats.level += 1
            self.sb.prep_level()

        
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
        
    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._aliens_change_direction()
                break

    def _aliens_change_direction(self):
        """将整群外星人下移，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_aliens(self, x_position, y_position):
        """创建一个外星人并放在当前行"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """检查是否有外星人位于屏幕边缘，并更新整个外星舰队的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检查是否有外星人击中飞船
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # 检查是否有外星人到达屏幕底端
        self._check_aliens_bottom()

    def _ship_hit(self):
        """响应飞船被外星人撞到"""
        if self.stats.ships_left > 0:
            # 将ship_left 减1
            self.stats.ships_left -= 1

            # 清空外星人和子弹列表
            self.bullets.empty()
            self.aliens.empty()

            # 创建一群新的外星人，并将飞船放到屏幕底端中央
            self._create_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self.game_active = False
            # 显示鼠标
            pygame.mouse.set_visible(True)


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

        # 显示得分
        self.sb.show_score()

        # 如果游戏处于非活动状态，就显示Play按钮
        if not self.game_active:
            self.play_button.draw_button()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        
    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # 像飞船被击中那样处理
                self._ship_hit()
                break

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
