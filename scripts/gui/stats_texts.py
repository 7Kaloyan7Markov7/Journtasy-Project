import pygame

import scripts.config.constants as const


class StatsUI:
    def __init__(self):
        self._font = pygame.font.SysFont('arial', const.STATS_UI_FONT_SIZE)
        self._visible = False
        self._surfaces = []
        self._bg_rect = None

    def update(self, player):
        self._visible = False
        if player is None or player.stats.is_dead: return

        stats = player.stats
        lines = [
            f"Level : {stats.level}",
            f"HP    : {int(stats.health.current_health)} / {int(stats.health.max_health)}",
            f"Armor : {int(stats.armor.armor)}",
            f"Damage: {int(stats.damage.damage)}",
        ]

        self._surfaces = [self._font.render(line, True, const.STATS_UI_TEXT_COLOR) for line in lines]

        line_h = self._surfaces[0].get_height()
        box_w = max(s.get_width() for s in self._surfaces) + const.STATS_UI_PADDING * 2
        box_h = len(self._surfaces) * (line_h + const.STATS_UI_LINE_SPACING) - const.STATS_UI_LINE_SPACING + const.STATS_UI_PADDING * 2

        box_x = const.SCREEN_WIDTH - box_w - const.STATS_UI_MARGIN
        box_y = const.STATS_UI_MARGIN
        self._bg_rect = pygame.Rect(box_x, box_y, box_w, box_h)
        self._visible = True

    def render(self, screen):
        if not self._visible: return

        pygame.draw.rect(screen, const.STATS_UI_BG_COLOR, self._bg_rect)
        pygame.draw.rect(screen, const.HEALTH_BAR_BORDER_COLOR, self._bg_rect, 1)

        line_h = self._surfaces[0].get_height()
        for i, surface in enumerate(self._surfaces):
            y = self._bg_rect.y + const.STATS_UI_PADDING + i * (line_h + const.STATS_UI_LINE_SPACING)
            screen.blit(surface, (self._bg_rect.x + const.STATS_UI_PADDING, y))
