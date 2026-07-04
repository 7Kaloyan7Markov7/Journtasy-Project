from scripts.entities.enemy import Enemy
from scripts.entities.obstacle import Obstacle
from scripts.entities.projectile import Projectile
from scripts.enums.enums import Direction, State
from scripts.managers.sound_manager import SoundManager
import scripts.config.constants as const


class CollisionManager:
    def manage_all_collisions(self, room):
        self._manage_weapon_enemy_collisions(room)
        self._manage_enemy_player_collisions(room)
        self._manage_player_obstacle_collisions(room)
        self._manage_enemy_obstacle_collisions(room)
        self._manage_projectile_collisions(room)
        self._manage_enemy_aggro_box(room)

    def manage_boundary_transition(self, room, dungeon_manager, scene_manager):
        player = room.player
        x, y = player.position.x, player.position.y

        if x <= const.SCREEN_LEFT_BOUNDARY:
            player.position.x = const.SCREEN_RIGHT_BOUNDARY - player.width - 1
            direction = Direction.LEFT
        elif x >= const.SCREEN_RIGHT_BOUNDARY - player.width:
            player.position.x = const.SCREEN_LEFT_BOUNDARY + 1
            direction = Direction.RIGHT
        elif y <= const.SCREEN_UPPER_BOUNDARY:
            player.position.y = const.SCREEN_LOWER_BOUNDARY - player.height - 1
            direction = Direction.UP
        elif y >= const.SCREEN_LOWER_BOUNDARY - player.height:
            player.position.y = const.SCREEN_UPPER_BOUNDARY + 1
            direction = Direction.DOWN
        else:
            return

        player.hitbox.move(player.position)
        dungeon_manager.transition_to_new_room(direction)
        scene_manager.current_scene.room = dungeon_manager.current_room
        
    def _manage_enemy_obstacle_collisions(self, room):
        enemies = [e for e in room.entity_list if isinstance(e, Enemy)]
        obstacles = [e for e in room.entity_list if isinstance(e, Obstacle)]

        for enemy in enemies:
            for obstacle in obstacles:
                if enemy.hitbox.is_colliding(obstacle.hitbox):
                    enemy.position.x = enemy.previous_position.x
                    enemy.position.y = enemy.previous_position.y
                    enemy.hitbox.move(enemy.position)
                    enemy.aggro_box.move(enemy.position)
                    break

    def _manage_enemy_player_collisions(self, room):
        player = room.player
        enemies = [e for e in room.entity_list if isinstance(e, Enemy)]

        for enemy in enemies:
            if enemy.stats.is_dead:
                continue

            if enemy.hitbox.is_colliding(player.hitbox):
                if enemy.attack_cooldown == 0:
                    enemy.state = State.ATTACKING
                    enemy.attack(player)
                elif not enemy.is_attacking:
                    enemy.state = State.IDLE

    def _manage_weapon_enemy_collisions(self, room):
        player = room.player
        weapon = player.weapon
        enemies = [e for e in room.entity_list if isinstance(e, Enemy)]

        if weapon.state != State.ATTACKING:
            return

        for enemy in enemies:
            if weapon.hitbox.is_colliding(enemy.hitbox):
                player.attack(enemy)

    def _manage_player_obstacle_collisions(self, room):
        player = room.player
        obstacles = [e for e in room.entity_list if isinstance(e, Obstacle)]

        for obstacle in obstacles:
            if player.hitbox.is_colliding(obstacle.hitbox):
                self._push_back(player)
                break

    def _manage_projectile_collisions(self, room):
        projectiles = [e for e in room.entity_list if isinstance(e, Projectile)]
        enemies = [e for e in room.entity_list if isinstance(e, Enemy)]
        obstacles = [e for e in room.entity_list if isinstance(e, Obstacle)]

        for projectile in projectiles:
            pos = projectile.position
            if (pos.x <= const.SCREEN_LEFT_BOUNDARY or
                    pos.x + projectile.width >= const.SCREEN_RIGHT_BOUNDARY or
                    pos.y <= const.SCREEN_UPPER_BOUNDARY or
                    pos.y + projectile.height >= const.SCREEN_LOWER_BOUNDARY):
                room.entity_list.remove(projectile)
                continue

            removed = False
            for obstacle in obstacles:
                if projectile.hitbox.is_colliding(obstacle.hitbox):
                    room.entity_list.remove(projectile)
                    removed = True
                    break

            if removed: continue

            for enemy in enemies:
                if projectile.hitbox.is_colliding(enemy.hitbox):
                    enemy.take_damage(projectile.damage)
                    if enemy.stats.is_dead:
                        projectile.owner.gain_experience(enemy.exp_on_kill)
                    room.entity_list.remove(projectile)
                    break

    def _manage_enemy_aggro_box(self, room):
        player = room.player
        if player.just_transitioned:
            return

        enemies = [e for e in room.entity_list if isinstance(e, Enemy) and not e.is_aggroed]

        for enemy in enemies:
            if enemy.aggro_box.is_colliding(player.hitbox):
                SoundManager.play_sound(const.ORC_SOUND)
                enemy.is_aggroed = True

    def _push_back(self, player):
        player.position.x = player.previous_position.x
        player.position.y = player.previous_position.y
        player.hitbox.move(player.position)