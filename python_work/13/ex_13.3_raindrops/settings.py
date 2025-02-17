class Settings:
    """存储雨滴的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.speed = 2.0
        self.drops_allowed = 3
        self.raindrop_speed = 1


        