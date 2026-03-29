from scripts.handlers.handler import Handler
from scripts.enums.enums import Direction, State
import scripts.config.constants as const


class GameplayHandler(Handler):
    def handle(self, game):
        scene = game.scene_manager.current_scene
        room = scene.room
        player = room.player

        self._handle_pause(scene, game.input_manager.pause_pressed)
        if scene.is_paused:
            return

        self._handle_player_movement(player, game.input_manager)
        self._handle_boundary_transition(game.scene_manager, game.dungeon_manager, player)
        room.collision_manager.manage_all_collisions(game.scene_manager.current_scene.room)

    def _handle_pause(self, scene, is_pause_pressed):
        if is_pause_pressed:
            scene.pause()

    def _handle_boundary_transition(self, scene_manager, dungeon_manager, player):
        direction = self._get_boundary_direction(player)
        if direction is None:
            return

        self._wrap_player_position(player, direction)
        dungeon_manager.transition_to_new_room(direction)
        scene_manager.current_scene.room = dungeon_manager.current_room

    def _get_boundary_direction(self, player):
        x, y = player.position.x, player.position.y
        if x <= const.SCREEN_LEFT_BOUNDARY:
            return Direction.LEFT
        if x >= const.SCREEN_RIGHT_BOUNDARY - player.width:
            return Direction.RIGHT
        if y <= const.SCREEN_UPPER_BOUNDARY:
            return Direction.UP
        if y >= const.SCREEN_LOWER_BOUNDARY - player.height:
            return Direction.DOWN
        return None

    def _wrap_player_position(self, player, direction):
        if direction == Direction.LEFT:
            player.position.x = const.SCREEN_RIGHT_BOUNDARY - player.width - 1
        elif direction == Direction.RIGHT:
            player.position.x = const.SCREEN_LEFT_BOUNDARY + 1
        elif direction == Direction.UP:
            player.position.y = const.SCREEN_LOWER_BOUNDARY - player.height - 1
        elif direction == Direction.DOWN:
            player.position.y = const.SCREEN_UPPER_BOUNDARY + 1

    def _handle_player_movement(self, player, input_manager):
        player.save_position()  # save before any movement for collision rollback

        moved = False
        if input_manager.move_left:
            player.move_left()
            moved = True
        if input_manager.move_right:
            player.move_right()
            moved = True
        if input_manager.move_up:
            player.move_up()
            moved = True
        if input_manager.move_down:
            player.move_down()
            moved = True

        player.state = State.MOVING if moved else State.IDLE
