import pygame

from entity import Entity
from asset_manager import AssetManager


class Projectile(Entity):
    def __init__(self, entity_id, position, velocity, hitbox):
        super().__init__(entity_id, position, velocity, hitbox)
        self.sprites = AssetManager.get_projectile_animations(entity_id)

    @property
    def current_image(self):
        return self.sprites[self.direction][self.current_frame_index]

    def update(self):
        ...

    def render(self, screen):
        screen.blit(self.current_image, self.position)