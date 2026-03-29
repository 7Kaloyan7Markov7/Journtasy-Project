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

            player.attack(entity)

    def manage_player_collisions(self, room):
        player = room.player
        entities = room.entity_list

        for entity in entities:
            if not player.hitbox.is_colliding(entity.hitbox): continue

            if isinstance(entity, Obstacle) and player.state == State.MOVING:
                self._push_back(player)
    

    def _push_back(self, player):
        player.position.x = player.previous_position.x
        player.position.y = player.previous_position.y
        player.hitbox.move(player.position)