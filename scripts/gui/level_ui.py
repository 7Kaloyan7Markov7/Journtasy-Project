import pygame

import scripts.config.constants as const


class LevelUI:
    def __init__(self):
        self._font = pygame.font.SysFont('arial', 16)

    def _get_level(self, entity):
        _text = f"{entity.stats.level}"

        entity_rect = entity.hitbox.hitbox
        level_x = int(entity_rect.centerx - const.HEALTH_BAR_WIDTH / 2 - 10)
        level_y = int(entity_rect.top - const.HEALTH_BAR_Y_OFFSET - 10)

        text_surface = self._font.render(_text, True, (255, 215, 0))
        text_rect = text_surface.get_rect(center = (level_x, level_y))

        return [text_surface, text_rect]

    def render(self, screen, entity):
        if entity.stats.is_dead: return
        text_surface, text_rect = self._get_level(entity)
        bg_rect = text_rect.inflate(6, 4)
        pygame.draw.rect(screen, (20, 20, 50), bg_rect)
        pygame.draw.rect(screen, const.HEALTH_BAR_BORDER_COLOR, bg_rect, 1)
        screen.blit(text_surface, text_rect)
        