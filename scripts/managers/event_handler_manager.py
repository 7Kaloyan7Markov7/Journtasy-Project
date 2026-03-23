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

    def quit_game_event(self, game):
        if game.input_manager.quit_pressed:
            game.running = False

    def handle(self, game):
        if game.scene_manager.current_scene.scene_id == const.MAIN_MENU_ID:
            self._main_menu_handler.handle(game)

        elif game.scene_manager.current_scene.scene_id == const.CHARACTER_SELECTION_ID:
            self._character_selection_handler.handle(game)

        elif game.scene_manager.current_scene.scene_id == const.GAME_SCENE_ID:
            self._gameplay_handler.handle(game)

        self.quit_game_event(game)   