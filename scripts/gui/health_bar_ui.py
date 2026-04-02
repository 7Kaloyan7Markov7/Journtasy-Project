import pygame

from scripts.gui.bar import Bar
import scripts.config.constants as const
    


class HealthBarUI(Bar):
    def __init__(self):
        super().__init__(const.HEALTH_BAR_WIDTH,
                        const.HEALTH_BAR_HEIGHT,
                        const.HEALTH_BAR_Y_OFFSET,
                        const.HEALTH_BAR_BORDER_COLOR,
                        const.HEALTH_BAR_BACKGROUND_COLOR,
                        const.HEALTH_BAR_FILL_COLOR)

    def update(self, entity):
        self._visible = False
        if entity is None or entity.stats.is_dead: return

        health = entity.stats.health
        max_hp = health.max_health

        if max_hp <= 0: return

        health_ratio = health.current_health / max_hp

        entity_rect = entity.hitbox.hitbox
        bar_x = int(entity_rect.centerx - self._width / 2)
        bar_y = int(entity_rect.top - self._y_offset)

        self._background_rect = pygame.Rect(bar_x, bar_y, self._width, self._height)
        self._fill_rect = pygame.Rect(bar_x, bar_y, int(self._width * health_ratio), self._height)
        self._visible = True

    def render(self, screen):
        if not self._visible: return

        super().render(screen)

