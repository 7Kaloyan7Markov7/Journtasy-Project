from scripts.entities.enemy import Enemy
from scripts.enums.enums import State


class CollisionManager:
    def manage_all_collisions(self, room):
        self.manage_weapon_enemy_collisions(room)


    def manage_weapon_enemy_collisions(self, room):
        entity_list = room.entity_list
        weapon = room.player.weapon

        for entity in entity_list:
            if not isinstance(entity, Enemy): continue
            if not weapon.hitbox.is_colliding(entity.hitbox): continue

            weapon.attack(entity)

    def manage_player_collisionxs(self, room):
        ...