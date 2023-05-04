import sys
import pygame
from settings import Settings
from bullet import Bullet
from ship import Ship


# 核心控制类,包含设置,屏幕,飞船,以及运行逻辑
class AlienInvasion:
    def __init__(self):
        pygame.init()
        # 从设置类获取屏幕设置
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # 设置背景
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")

        # 创建一艘飞船
        self.ship = Ship(self)

        # 编组
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            # 监视键盘和鼠标事件
            self._check_events()
            # 不断更新飞船的位置
            self.ship.update()
            # 更新子单信息
            self._update_bullets()
            # 重绘屏幕
            self._update_screen()

    # 辅助方法 在类中执行任务，但并非是通过实例调用的。在
    # Python中，辅助方法的名称以单个下划线打头。
    def _check_events(self):
        """响应按键和鼠标事件"""
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:  # 退出事件
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 按下事件
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # 松开事件
                self._check_keyup_events(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # 调用ship.blitme() 将飞船绘制到屏幕上，确保它出现在背景前面
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def _check_keydown_events(self, event):
        """响应按键。"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        # 限制子单数量
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """响应松开。"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        self.bullets.update()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:  # 删除屏幕外已消失的子弹
                self.bullets.remove(bullet)

        # print(len(self.bullets))


if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
