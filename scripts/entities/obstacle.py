from scripts.entities.entity import Entity
from scripts.managers.asset_manager import AssetManager
from scripts.collisions.hitbox import HitBox
import scripts.config.constants as const
import pygame


class Obstacle(Entity):
    def __init__(self, entity_id, position, speed):
        super().__init__(entity_id, position, speed)
        self._image = AssetManager.get_obstacle_image(entity_id)

        hitbox_data = const.HITBOX_DATA[const.OBSTACLE_ID][entity_id]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

    @property
    def image(self):
        return self._image

    @property
    def is_blocking(self):
        return self._is_blocking

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, self.position)
        pygame.draw.rect(screen, self._hitbox.width, self._hitbox._hitbox)