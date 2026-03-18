from scripts.enums.enums import Direction
from scripts.handlers.handler import Handler
from scripts.handlers.gameplay_handler import GameplayHandler
from scripts.handlers.character_selection_handler import CharSelHandler
from scripts.handlers.menu_handler import MenuHandler
import scripts.constants.constants as const


class EventHandlerManager(Handler):
    def __init__(self):
        self._gameplay_handler = GameplayHandler()
        self._character_selection_handler = CharSelHandler()
        self._main_menu_handler = MenuHandler()

    def pause_event(self, scene, is_pause_clicked):
        if is_pause_clicked:
            scene.pause()

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
    
    def chosen_player_event(self, scene, user_click_position):
        player_choice = self.choosing_character_event(scene, user_click_position) 
        if player_choice is not None:
            return player_choice
        
        return None


    def start_game_event(self, scene, user_input):
        ...

    def quit_game_event(self, game, quit_pressed):
        if quit_pressed:
            game.running = False

    def quit_game_menu_event(self, game, scene, user_click_position):
        if scene.exit_button.is_clicked(user_click_position):
            game.running = False

    def room_transition_event(self, dungeon_manager, direction):
        dungeon_manager.transition_to_new_room(direction)

    def handle_main_menu(self, game):
        ...

    def handle_character_selection(self, game):
        self.choosing_character_event()

    def handle_gameplay(self, game):
        self.player_stepped_bounds_event(game.scene_manager.scene.room.player)
        self.pause_event(game.scene,game.input_manager.pause_pressed)

    def handle(self, game):
        if game.scene_manager.current_scene.scene_id == const.MAIN_MENU_ID:
            self._main_menu_handler.handle(game)

        if game.scene_manager.current_scene.scene_id == const.CHARACTER_SELECTION_ID:
            self._character_selection_handler.handle(game)

        if game.scene_manager.current_scene.scene_id == const.GAME_SCENE_ID:
            self.handle_gameplay(game)   