from scripts.entities.entity import Entity
from scripts.managers.asset_manager import AssetManager
from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import State
import scripts.config.constants as const


class Weapon(Entity):
    def __init__(self, entity_id, position, speed):
        super().__init__(entity_id, position, speed)
        self._sprites = AssetManager.get_weapon_animations(entity_id)

        hitbox_data = const.HITBOX_DATA[const.WEAPON_ID][entity_id]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

    @property
    def current_image(self):
        return self._sprites[self.direction][self.current_frame_index]
    
    def attack(self, room, player):
        self._state = State.ATTACKING

        if len(room.entity_list) == 0:
            return

        for entity in room.entity_list:
            if entity.entity_id in const.ENEMY_IDS:
                if self._hitbox.is_colliding(entity.hitbox):
                    entity.take_damage(player.stats.damage.value)

    def update(self):
        ...

    def render(self, screen):
        screen.blit(self.current_image, self.position)