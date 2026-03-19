from scripts.handlers.handler import Handler
from scripts.managers.dungeon_manager import DungeonManager
import scripts.config.constants as const


class CharSelHandler(Handler):
    def handle(self, game):
        current_scene = game.scene_manager.current_scene
        left_click_position = game.input_manager.left_click_position

        player_choice = self.chosen_player_event(current_scene, left_click_position)
        if player_choice is not None:
            self.start_gameplay_event(game, player_choice)

    def chosen_player_event(self, current_scene, left_click_position):
        return self.choosing_character_event(current_scene, left_click_position)

    def choosing_character_event(self, scene, left_click_position):
        if left_click_position is None:
            return None

        if scene.knight_button.is_clicked(left_click_position):
            return const.KNIGHT_ID

        if scene.boxer_button.is_clicked(left_click_position):
            return const.BOXER_ID

        if scene.wizard_button.is_clicked(left_click_position):
            return const.WIZARD_ID

        if scene.monk_button.is_clicked(left_click_position):
            return const.MONK_ID

        if scene.killer_button.is_clicked(left_click_position):
            return const.KILLER_ID

        if scene.caveman_button.is_clicked(left_click_position):
            return const.CAVEMAN_ID

        return None

    def start_gameplay_event(self, game, player_choice):
        game.dungeon_manager = DungeonManager(player_choice)
        game.scene_manager.set_game_scene(game.dungeon_manager.current_room)
        game.scene_manager.open_game_scene()