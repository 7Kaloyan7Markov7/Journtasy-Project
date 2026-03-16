import pygame

from hitbox import HitBox
import constants as const


class Button:
    def __init__(self, text, button_id):
        self._button_id = button_id
        button_data = const.BUTTONS_DATA[button_id]

        self._click_box = HitBox(button_data[0] , button_data[1], button_data[2])
        self._text = text
        
    @property
    def click_box(self):
        return self._click_box

    def is_clicked(self, click_point):
        return self.click_box.hitbox.collidepoint(click_point)
    
    def render(self, screen):
        return