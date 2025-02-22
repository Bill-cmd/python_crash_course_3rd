class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed = 10
        self.ship_limit = 3
        # 子弹的参数
        '''
        self.bullet_speed = 1.5
        self.bullet_color = (60, 60, 60)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_allowed = 3
        '''
        # 子弹作弊的设定
        self.bullet_speed = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_allowed = 10

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        

