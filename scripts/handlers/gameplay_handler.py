from scripts.handlers.handler import Handler
from scripts.entities.enemy import Enemy
from scripts.enums.enums import State


class GameplayHandler(Handler):
    def handle(self, game):
        scene = game.scene_manager.current_scene
        room = scene.room
        player = room.player

        self._handle_pause(scene, game.input_manager.pause_pressed)
        if scene.is_paused:
            return

        self._handle_player_movement(player, game.input_manager)
        self._handle_player_attack(player, game.input_manager.attack_pressed)
        room.collision_manager.manage_boundary_transition(room, game.dungeon_manager, game.scene_manager)
        self._handle_enemies(room)
        room.collision_manager.manage_all_collisions(game.scene_manager.current_scene.room)

    def _handle_enemies(self, room):
        player = room.player
        if player is None:
            return
        
        enemies = [e for e in room.entity_list if isinstance(e, Enemy)]

        for enemy in enemies:
            if enemy.stats.is_dead:
                continue

            if enemy.is_aggroed:
                enemy.move(player)

            enemy.update()

    def _handle_pause(self, scene, is_pause_pressed):
        if is_pause_pressed:
            scene.pause()

    def _handle_player_attack(self, player, is_attack_pressed):
        if is_attack_pressed:
            player.attack()

    def _handle_player_movement(self, player, input_manager):
        player.save_position()

        if player.state == State.MOVING:
            player.state = State.IDLE

        if input_manager.move_left:
            player.move_left()
            
        if input_manager.move_right:
            player.move_right()

        if input_manager.move_up:
            player.move_up()

        if input_manager.move_down:
            player.move_down()
