import pygame

from character import Character
from asset_manager import AssetManager


class Player(Character):
    def __init__(self, entity_id, position, velocity, hitbox, stats, weapon):
        super().__init__(entity_id, position, velocity, hitbox, stats)
        self.experience_bar = 0
        self.weapon = weapon
        self.sprites = AssetManager.get_player_animations(entity_id)

    @property
    def current_image(self):
        return self.sprites[self.direction][self.current_frame_index]

    def update(self):
        ...

    def render(self, screen):
        screen.blit(self.current_image, self.position)
        self.weapon.render(screen)

    def attack(self):
        pass

    def move(self):
        pass