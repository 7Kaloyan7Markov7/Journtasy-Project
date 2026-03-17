from character import Character
from asset_manager import AssetManager
from hitbox import HitBox
import constants as const


class Enemy(Character):
    def __init__(self, entity_id, position, speed, level):
        super().__init__(entity_id, position, speed, level)

        self._sprites = AssetManager.get_enemy_animations(entity_id)

        hitbox_data = const.HITBOX_DATA[const.ENEMY_ID][entity_id]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

    @property
    def current_image(self):
        return self._sprites[self.direction][self.current_frame_index]

    def update(self):
        super().update()

    def render(self, screen):
        screen.blit(self.current_image, self.position)

    def attack(self):
        pass

    def move(self):
        pass