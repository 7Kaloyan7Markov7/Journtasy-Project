import pygame


class HealthBarUI:
    def __init__(
        self,
        width=40,
        height=7,
        y_offset=8,
        border_color=(0, 0, 0),
        background_color=(120, 0, 0),
        fill_color=(0, 200, 0),
    ):
        self._width = width
        self._height = height
        self._y_offset = y_offset

        self._border_color = border_color
        self._background_color = background_color
        self._fill_color = fill_color

    def update(self, entity):
        self._visible = False
        if entity is None or entity.stats.is_dead:
            return

        health = entity.stats.health
        max_hp = health.max_health
        if max_hp <= 0:
            return

        health_ratio = max(0, min(1, health.current_health / max_hp))

        entity_rect = entity.hitbox.hitbox
        bar_x = int(entity_rect.centerx - self._width / 2)
        bar_y = int(entity_rect.top - self._y_offset)

        self._background_rect = pygame.Rect(bar_x, bar_y, self._width, self._height)
        self._fill_rect = pygame.Rect(bar_x, bar_y, int(self._width * health_ratio), self._height)
        self._visible = True

    def render(self, screen):
        if not self._visible:
            return

        pygame.draw.rect(screen, self._background_color, self._background_rect)
        pygame.draw.rect(screen, self._fill_color, self._fill_rect)
        pygame.draw.rect(screen, self._border_color, self._background_rect, 1)

