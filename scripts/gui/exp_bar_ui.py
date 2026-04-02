import pygame

from scripts.gui.bar import Bar
import scripts.config.constants as const

class ExpBar(Bar):
    def __init__(self):
        super().__init__(const.EXP_BAR_WIDTH,
                        const.EXP_BAR_HEIGHT,
                        const.EXP_BAR_Y_OFFSET,
                        const.EXP_BAR_BORDER_COLOR,
                        const.EXP_BAR_BACKGROUND_COLOR,
                        const.EXP_BAR_FILL_COLOR)

    def update(self, player):
        self._visible = False
        if player.stats.is_dead: return

        exp_ratio = player.current_experience / player.exp_threshold
        player_rect = player.hitbox.hitbox
        bar_x = int(player_rect.centerx - self._width / 2)
        bar_y = int(player_rect.top - self._y_offset)

        self._background_rect = pygame.Rect(bar_x, bar_y, self._width, self._height)
        self._fill_rect = pygame.Rect(bar_x, bar_y, int(self._width * exp_ratio), self._height)
        self._visible = True


    def render(self, screen):
        super().render(screen)