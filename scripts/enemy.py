from character import Character
from asset_manager import AssetManager


class Enemy(Character):
    def __init__(self, entity_id, position, velocity, hitbox, stats):
        super().__init__(entity_id, position, velocity, hitbox, stats)
        self.sprites = AssetManager.get_enemy_animations(entity_id)

    def update(self):
        ...

    def render(self, screen):
        ...