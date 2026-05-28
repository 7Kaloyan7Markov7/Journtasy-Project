from scripts.scenes.scene import Scene
from scripts.building_blocks.button import Button
import scripts.config.constants as const


class CharacterSelection(Scene):
    scene_id = const.CHARACTER_SELECTION_ID

    def __init__(self):
        self._knight_button = Button(const.KNIGHT_BUTTON_TEXT, const.KNIGHT_BUTTON_ID)
        self._wizard_button = Button(const.WIZARD_BUTTON_TEXT, const.WIZARD_BUTTON_ID)
        self._monk_button = Button(const.MONK_BUTTON_TEXT, const.MONK_BUTTON_ID)
        self._killer_button = Button(const.KILLER_BUTTON_TEXT, const.KILLER_BUTTON_ID)

    @property
    def knight_button(self):
        return self._knight_button

    @property
    def wizard_button(self):
        return self._wizard_button

    @property
    def monk_button(self):
        return self._monk_button

    @property
    def killer_button(self):
        return self._killer_button

    def render(self, screen):
        self.knight_button.render(screen)
        self.wizard_button.render(screen)
        self.monk_button.render(screen)
        self.killer_button.render(screen)