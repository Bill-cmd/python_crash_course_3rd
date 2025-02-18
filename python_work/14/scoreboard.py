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
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        