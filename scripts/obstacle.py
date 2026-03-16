from entity import Entity
from asset_manager import AssetManager
from hitbox import HitBox
import constants as const


class Obstacle(Entity):
    def __init__(self, entity_id, position, speed, is_blocking):
        super().__init__(entity_id, position, speed)
        self._image = AssetManager.get_obstacle_image(entity_id)
        self._is_blocking = is_blocking
        hitbox_data = const.HITBOX_DATA[const.OBSTACLE_ID][entity_id]
        self.hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

    @property
    def image(self):
        return self._image

    def update(self):
        ...

    def render(self, screen):
        screen.blit(self.image, self.position)