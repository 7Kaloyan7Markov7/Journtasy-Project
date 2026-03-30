from scripts.entities.enemy import Enemy
from scripts.entities.obstacle import Obstacle
from scripts.entities.projectile import Projectile
from scripts.enums.enums import State


class CollisionManager:
    def manage_all_collisions(self, room):
        self._manage_weapon_enemy_collisions(room)
        self._manage_player_obstacle_collisions(room)
        self._manage_projectile_collisions(room)

    def _manage_weapon_enemy_collisions(self, room):
        player = room.player
        weapon = player.weapon
        enemies = [e for e in room.entity_list if isinstance(e, Enemy)]

        if weapon.state != State.ATTACKING:
            return

        for enemy in enemies:
            if weapon.hitbox.is_colliding(enemy.hitbox):
                weapon.apply_damage(enemy, player.stats.damage.damage)

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

        for projectile in projectiles:
            for enemy in enemies:
                if projectile.hitbox.is_colliding(enemy.hitbox):
                    enemy.take_damage(projectile.damage)
                    room.entity_list.remove(projectile)
                    break

    def _push_back(self, player):
        player.position.x = player.previous_position.x
        player.position.y = player.previous_position.y
        player.hitbox.move(player.position)