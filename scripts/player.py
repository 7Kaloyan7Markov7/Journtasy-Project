from character import Character
from asset_manager import AssetManager


class Player(Character):
    def __init__(self, entity_id, position, velocity, hitbox, stats):
        super().__init__(entity_id, position, velocity, hitbox, stats)


    def update(self):
        ...

    def render(self):
        ...