from scripts.enums.enums import Direction
from scripts.handlers.handler import Handler
from scripts.handlers.gameplay_handler import GameplayHandler
from scripts.handlers.character_selection_handler import CharSelHandler
from scripts.handlers.menu_handler import MenuHandler
import scripts.config.constants as const


class EventHandlerManager(Handler):
    def __init__(self):
        self._gameplay_handler = GameplayHandler()
        self._character_selection_handler = CharSelHandler()
        self._main_menu_handler = MenuHandler()
    
    def chosen_player_event(self, current_scene, user_click_position):
        player_choice = self.choosing_character_event(current_scene, user_click_position) 
        if player_choice is not None:
            return player_choice
        
        return None


    def start_game_event(self, current_scene, user_input):
        ...

    def quit_game_event(self, game):
        if game.input_manager.quit_pressed:
            game.running = False

    def handle(self, game):
        if game.scene_manager.current_scene.scene_id == const.MAIN_MENU_ID:
            self._main_menu_handler.handle(game)

        if game.scene_manager.current_scene.scene_id == const.CHARACTER_SELECTION_ID:
            self._character_selection_handler.handle(game)

        if game.scene_manager.current_scene.scene_id == const.GAME_SCENE_ID:
            self._gameplay_handler.handle(game)

        self.quit_game_event(game)   