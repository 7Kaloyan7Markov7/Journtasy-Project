from scripts.handlers.handler import Handler
from scripts.enums.enums import Direction, State
import scripts.config.constants as const


class GameplayHandler(Handler):
    def handle(self, game):
        self.pause_event(game.scene_manager.current_scene, game.input_manager.pause_pressed)
        player = game.scene_manager.current_scene.room.player
        if game.scene_manager.current_scene.is_paused:
            return

        self.player_stepped_bounds_event(game.scene_manager, game.dungeon_manager, player)
        self.player_movement_event(player, game.input_manager)
        game.scene_manager.current_scene.room.collision_manager.manage_all_collisions(game.scene_manager.current_scene.room)
        
    def pause_event(self, scene, is_pause_clicked):
        if is_pause_clicked:
            scene.pause()

    def player_stepped_bounds_event(self, scene_manager, dungeon_manager, player):
        
        if player.position.x <= const.SCREEN_LEFT_BOUNDARY:
            player.position.x = const.SCREEN_RIGHT_BOUNDARY - player.width - 1
            dungeon_manager.transition_to_new_room(Direction.LEFT)

        elif player.position.x >= const.SCREEN_RIGHT_BOUNDARY - player.width :
            player.position.x = const.SCREEN_LEFT_BOUNDARY + 1
            dungeon_manager.transition_to_new_room(Direction.RIGHT)

        elif player.position.y <= const.SCREEN_UPPER_BOUNDARY:
            player.position.y = const.SCREEN_LOWER_BOUNDARY - player.height - 1
            dungeon_manager.transition_to_new_room(Direction.UP)

        elif player.position.y >= const.SCREEN_LOWER_BOUNDARY - player.height:
            player.position.y = const.SCREEN_UPPER_BOUNDARY + 1
            dungeon_manager.transition_to_new_room(Direction.DOWN)
        
        scene_manager.current_scene.room = dungeon_manager.current_room

    
    def player_movement_event(self, player, input_manager):
        move_left = input_manager.move_left
        move_right = input_manager.move_right
        move_up = input_manager.move_up
        move_down = input_manager.move_down

        player._previous_position = player.position.copy()  # save before moving

        if move_left:
            player.move_left()
        if move_right:
            player.move_right()
        if move_up:
            player.move_up()
        if move_down:
            player.move_down()

        if move_left or move_right or move_up or move_down:
            player.state = State.MOVING
        else:
            player.state = State.IDLE


    def enemy_attack_event(self, game):
        ...
    
    def player_attack_event(self, game):
        ...

    def enemy_take_damage_event(self, game):
        ...

    def player_take_damage_event(self, game):
        ...
    
    def player_shoot_event(self, game):
        ...    