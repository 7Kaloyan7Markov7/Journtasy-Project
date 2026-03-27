from scripts.entities.character import Character
from scripts.managers.asset_manager import AssetManager
from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import Direction
import scripts.config.constants as const


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
        self.move()
        self.animate()

    def render(self, screen):
        screen.blit(self.current_image, self.position)

    def attack(self, target):
        pass

    def move(self):
        pass