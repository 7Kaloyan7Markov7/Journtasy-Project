from scripts.handlers.handler import Handler
from scripts.managers.dungeon_manager import DungeonManager
import scripts.config.constants as const


class CharSelHandler(Handler):
    def handle(self, game):
        current_scene = game.scene_manager.current_scene
        left_click_position = game.input_manager.left_click_position

        player_choice = self._get_clicked_character(current_scene, left_click_position)
        if player_choice is not None:
            self._start_gameplay(game, player_choice)

    def _get_clicked_character(self, scene, click_position):
        if click_position is None:
            return None

        for button_attr, character_id in const.BUTTON_CHARACTER_MAP.items():
            button = getattr(scene, button_attr)
            if button.is_clicked(click_position):
                return character_id

        return None

    def _start_gameplay(self, game, player_choice):
        game.dungeon_manager = DungeonManager(player_choice)
        game.scene_manager.set_game_scene(game.dungeon_manager.current_room)
        game.scene_manager.open_game_scene()
