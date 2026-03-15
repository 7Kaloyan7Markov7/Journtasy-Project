from input_manager import InputManager
import constants as const


class EventHandler:
    def pause_event(self, scene, user_input):
        if scene.scene_id == const.GAME_SCENE_ID and user_input.pause_pressed:
            scene.pause()

    def start_game_event(self, scene, user_input):
        ...

    def quit_game_event(self, user_input):
        ...

    def quit_game_menu_event(self, scene, user_input):
        ...
    
    def handle(self, game):
        ...

    