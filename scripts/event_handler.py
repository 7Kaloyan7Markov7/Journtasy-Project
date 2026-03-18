from input_manager import InputManager
from dungeon_manager import DungeonManager
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

    def player_stepped_bounds_event(self, player):
        if player.position.x <= const.SCREEN_LEFT_BOUNDARY:
            player.position.x = const.SCREEN_RIGHT_BOUNDARY - player.width
            self.change_room_event()

        elif player.position.x >= const.SCREEN_RIGHT_BOUNDARY - player.width:
            player.position.x = const.SCREEN_LEFT_BOUNDARY
            self.change_room_event()

        elif player.position.y <= const.SCREEN_UPPER_BOUNDARY:
            player.position.y = const.SCREEN_LOWER_BOUNDARY - player.height
            self.change_room_event()

        elif player.position.y >= const.SCREEN_LOWER_BOUNDARY - player.height:
            player.position.y = const.SCREEN_UPPER_BOUNDARY
            self.change_room_event()

    def change_room_event(self, dungeon_manager):
        dungeon_manager.create_new_room

    def handle(self, game):
        ...
    