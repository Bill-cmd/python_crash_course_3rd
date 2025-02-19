import pygame.font

class Scoreboard:
    """显示得分信息的类"""

    def __init__(self, ai_game):
        """初始化得分属性"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        self.prep_score()
        # 准备最高得分图像
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """将得分转换为渲染的图像"""
        # 将得分格式化为一个字符串round() 函数通常让浮点数（第⼀个实参）精确到⼩数点后某⼀位，其中的⼩数位数由第⼆个实参指定。
        # 如果将第⼆个实参指定为负数，round()会将第⼀个实参舍⼊到最近的 10 的整数倍（如 round(98.4, -1) 得到的结果是 90）。
        rounded_score = round(self.stats.score, -1)
        # 将整数按千位分割，用,分隔，然后转换为字符串
        score_str = f"{rounded_score:,}"
        # 获取得分的字符串格式
        #score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        # 右边缘与屏幕右边缘相距 20 像素
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
         """在屏幕上显示当前得分和最高得分及等级"""
         self.screen.blit(self.score_image, self.score_rect)
         self.screen.blit(self.high_score_image, self.high_score_rect)
         # 显示等级
         self.screen.blit(self.level_image, self.level_rect)
    
    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def check_high_score(self):
        """检查是否需要更新最高得分图像"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """将等级转换为渲染的图像"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
