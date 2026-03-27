from pygame import Vector2

from scripts.entities.enemy import Enemy
from scripts.enums.enums import Direction


class CollisionManager:
    def manage_all_collisions(self, room):
        self.manage_weapon_enemy_collisions(room)
        self.manage_player_collisions(room)


    def manage_weapon_enemy_collisions(self, room):
        entity_list = room.entity_list
        weapon = room.player.weapon

        for entity in entity_list:
            if not isinstance(entity, Enemy): continue
            if not weapon.hitbox.is_colliding(entity.hitbox): continue

            weapon.attack(entity)

    def manage_player_collisions(self, room):
        player = room.player
        entities = room.entity_list

        for entity in entities:
            if player.hitbox.is_colliding(entity.hitbox):
                if player.direction == Direction.DOWN:
                    player.position += Vector2(0, -player.speed)
                elif player.direction == Direction.UP:
                    player.position += Vector2(0, player.speed)
                elif player.direction == Direction.RIGHT:
                    player.position += Vector2(-player.speed, 0)
                elif player.direction == Direction.LEFT:
                    player.position += Vector2(player.speed, 0)

