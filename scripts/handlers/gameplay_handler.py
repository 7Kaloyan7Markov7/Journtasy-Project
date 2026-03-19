from scripts.handlers.handler import Handler
from scripts.enums.enums import Direction
import scripts.config.constants as const


class GameplayHandler(Handler):
    def handle(self, game):
        self.pause_event(game.scene_manager.current_scene, game.input_manager.pause_pressed)
        self.player_stepped_bounds_event( game.scene_manager, game.dungeon_manager, game.scene_manager.current_scene.room.player)


    def pause_event(self, scene, is_pause_clicked):
        if is_pause_clicked:
            scene.pause()

    def player_stepped_bounds_event(self, scene_manager, dungeon_manager, player):
        
        if player.position.x <= const.SCREEN_LEFT_BOUNDARY:
            player.position.x = const.SCREEN_RIGHT_BOUNDARY - player.width
            dungeon_manager.transition_to_new_room(Direction.LEFT)

        elif player.position.x >= const.SCREEN_RIGHT_BOUNDARY - player.width:
            player.position.x = const.SCREEN_LEFT_BOUNDARY
            dungeon_manager.transition_to_new_room(Direction.RIGHT)

        elif player.position.y <= const.SCREEN_UPPER_BOUNDARY:
            player.position.y = const.SCREEN_LOWER_BOUNDARY - player.height
            dungeon_manager.transition_to_new_room(Direction.UP)

        elif player.position.y >= const.SCREEN_LOWER_BOUNDARY - player.height:
            player.position.y = const.SCREEN_UPPER_BOUNDARY
            dungeon_manager.transition_to_new_room(Direction.DOWN)
        
        scene_manager.current_scene.room = dungeon_manager.current_room

    def enemy_attack_event(self, game):
        ...
    
    def player_attack_event(self, game):
        ...

    def player_take_damage_event(self, game):
        ...
    
    def player_shoot_event(self, game):
        ...    