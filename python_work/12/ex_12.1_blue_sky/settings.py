class Settings:
    """存储blue_sky的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)
        # 飞船设置
        self.ship_speed = 1.5

