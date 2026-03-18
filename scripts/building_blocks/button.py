import pygame

from scripts.collisions.hitbox import HitBox
import scripts.config.constants as const


class Button:
    def __init__(self, text, button_id):
        self._button_id = button_id
        button_data = const.BUTTONS_DATA[button_id]

        self._click_box = HitBox(button_data[0] , button_data[1], button_data[2])
        self._text = text
        self._font = pygame.font.SysFont(const.BUTTON_FONT_NAME, const.BUTTON_FONT_SIZE)
        
    @property
    def click_box(self):
        return self._click_box

    def is_clicked(self, click_point):
        return self.click_box.hitbox.collidepoint(click_point)
    
    def render(self, screen):
        rect = self.click_box.hitbox

        pygame.draw.rect(screen, const.BUTTON_COLOR, rect)
        pygame.draw.rect(screen, const.BUTTON_BORDER_COLOR, rect, const.BUTTON_BORDER_WIDTH)

        text_surface = self._font.render(self._text, True, const.BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)

        screen.blit(text_surface, text_rect)