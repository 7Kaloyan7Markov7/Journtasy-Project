from scripts.handlers.handler import Handler
import scripts.config.constants as const


class CharSelHandler(Handler):
    def handle(self, game):
        ...

    def choosing_character_event(self, scene, user_click_position):
        if scene.knight_button.is_clicked(user_click_position):
            return const.KNIGHT_ID

        if scene.boxer_button.is_clicked(user_click_position):
            return const.BOXER_ID

        if scene.wizard_button.is_clicked(user_click_position):
            return const.WIZARD_ID

        if scene.monk_button.is_clicked(user_click_position):
            return const.MONK_ID

        if scene.killer_button.is_clicked(user_click_position):
            return const.KILLER_ID

        if scene.caveman_button.is_clicked(user_click_position):
            return const.CAVEMAN_ID

        return None    