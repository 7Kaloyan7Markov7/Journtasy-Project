from scripts.entities.enemy import Enemy
from scripts.entities.obstacle import Obstacle
from scripts.entities.projectile import Projectile
from scripts.enums.enums import State


class CollisionManager:
    def manage_all_collisions(self, room):
        self._manage_weapon_enemy_collisions(room)
        self._manage_enemy_player_collisions(room)
        self._manage_player_obstacle_collisions(room)
        self._manage_enemy_obstacle_collisions(room)
        self._manage_projectile_collisions(room)
        self._manage_enemy_aggro_box(room)

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
                enemy.attack(player)

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

        for projectile in projectiles:
            for enemy in enemies:
                if projectile.hitbox.is_colliding(enemy.hitbox):
                    enemy.take_damage(projectile.damage)
                    room.entity_list.remove(projectile)
                    break

    def _manage_enemy_aggro_box(self, room):
        player = room.player
        enemies = [e for e in room.entity_list if isinstance(e, Enemy) and not e.is_aggroed]
        
        for enemy in enemies:
            if enemy.aggro_box.is_colliding(player.hitbox):
                enemy.is_aggroed = True

    def _push_back(self, player):
        player.position.x = player.previous_position.x
        player.position.y = player.previous_position.y
        player.hitbox.move(player.position)