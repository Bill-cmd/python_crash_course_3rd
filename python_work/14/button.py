import pygame.font

class Button:
    """创建按钮的类"""

    def __init__(self, ai_game, msg):
        """初始化按钮的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只创建一次
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        # font.render() ⽅法接受⼀个布尔实参，该实参指定是否开启反锯⻮功能,余下的两个实参分别是⽂本颜⾊和背景⾊
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个填充的按钮，再绘制文本"""
        # 调⽤ screen.fill() 来绘制表⽰按钮的矩形
        self.screen.fill(self.button_color, self.rect)
        # 调⽤ screen.blit()来向它传递⼀幅图像以及与该图像相关联的 rect，从⽽在屏幕上绘制⽂本图像
        self.screen.blit(self.msg_image, self.msg_image_rect)
