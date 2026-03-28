from pygame import Vector2

from scripts.entities.enemy import Enemy
from scripts.entities.obstacle import Obstacle
from scripts.enums.enums import Direction, State


class CollisionManager:
    def manage_all_collisions(self, room):
        self.manage_weapon_enemy_collisions(room)
        self.manage_player_collisions(room)

    def manage_weapon_enemy_collisions(self, room):
        player = room.player
        weapon = player.weapon
        entity_list = room.entity_list

        for entity in entity_list:
            if not isinstance(entity, Enemy): continue
            if not weapon.hitbox.is_colliding(entity.hitbox): continue

            player.attack(entity)  # pass player so damage calc works

    def manage_player_collisions(self, room):
        if room.player.state != State.MOVING: return

        player = room.player
        entities = room.entity_list

        for entity in entities:
            if not player.hitbox.is_colliding(entity.hitbox): continue

            if isinstance(entity, Obstacle):
                self._push_back(player)

            elif isinstance(entity, Enemy):
                entity.attack(player)
    

    def _push_back(self, player):
        if player.direction == Direction.DOWN:
            player.position.y -= player.speed
        elif player.direction == Direction.UP:
            player.position.y += player.speed
        elif player.direction == Direction.RIGHT:
            player.position.x -= player.speed
        elif player.direction == Direction.LEFT:
            player.position.x += player.speed
        
        player.hitbox.move(player.position)