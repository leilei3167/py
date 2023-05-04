import pygame


class Ship:
    def __init__(self, ai_game):  # AlienInvasion的实例,便于获取设置和屏幕
        self.settings = ai_game.settings

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()  # 整个屏幕的矩形

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()  # 获取飞船的矩形

        # 对于每艘新飞船，都将其放在屏幕底部的中央,处理元素的位置可以使用矩形的属性top、bottom、left和right，他们分别是相应矩形边缘的y坐标和x坐标
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # 移动标志 玩家按下右箭头键时，我们
        # 将该标志设置为True ，在玩家松开时将该标志重新设置为False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 因为rect只能是整数的值,不直接更新rect的值，而是更新self.x的值，再将self.x的值赋给rect.x
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船

                Pygame之所以高效，是因为它让你能够像处理矩形（rect 对象）一样处理所有的
        游戏元素，即便其形状并非矩形。像处理矩形一样处理游戏元素之所以高效，是因
        为矩形是简单的几何形状。例如，通过将游戏元素视为矩形，Pygame能够更快地判
        断出它们是否发生了碰撞。这种做法的效果通常很好，游戏玩家几乎注意不到我们
        处理的并不是游戏元素的实际形状。在这个类中，我们将把飞船和屏幕作为矩形进
        行处理。

        """
        self.screen.blit(self.image, self.rect)
