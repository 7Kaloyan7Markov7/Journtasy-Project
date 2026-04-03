import pygame

import scripts.config.constants as const


class LevelUI:
    def __init__(self):
        self._font = pygame.font.SysFont('arial', 16)

    def _get_level(self, entity):
        _text = f"{entity.stats.level}"

        entity_rect = entity.hitbox.hitbox
        level_x = int(entity_rect.centerx - const.HEALTH_BAR_WIDTH / 2 - 10)
        level_y = int(entity_rect.top - 5)

        

        text_surface = self._font.render(_text, True, (0,0,255), (255,255,255))
        text_rect = text_surface.get_rect(center = (level_x, level_y))

        return [text_surface, text_rect]

    def render(self, screen, entity):
        text_and_rect = self._get_level(entity) 
        screen.blit(text_and_rect[0], text_and_rect[1])
        