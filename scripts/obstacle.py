from entity import Entity
from asset_manager import AssetManager


class Obstacle(Entity):
    def __init__(self, entity_id, position, velocity, hitbox, is_blocking):
        super().__init__(entity_id, position, velocity, hitbox)
        self.sprites = AssetManager.get_obstacle_image[entity_id]
        self.is_blocking = is_blocking

    def update(self):
        ...

    def render(self):
        ...