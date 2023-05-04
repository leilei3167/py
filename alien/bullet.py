import pygame
from pygame.sprite import Sprite


# 继承sprite，可将游戏中相关的元素编组，进而同时操作编组中的所有元素
class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置,子弹并非基于图像，因此必须使用
        # pygame.Rect() 类从头开始创建一个矩形
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        # 子弹的初始位置取决于飞船当前的
        # 位置
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        # 更新表示子弹位置的小数值
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
