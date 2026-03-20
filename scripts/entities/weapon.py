from scripts.entities.animated_entity import AnimatedEntity
from scripts.managers.asset_manager import AssetManager
from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import State, Direction
import scripts.config.constants as const
import pygame


class Weapon(AnimatedEntity):
    def __init__(self, entity_id, position, speed):
        super().__init__(entity_id, position, speed)
        self._sprites = AssetManager.get_weapon_animations(entity_id)

        hitbox_data = const.HITBOX_DATA[const.WEAPON_ID][entity_id]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

        self._left_offset = pygame.Vector2(-20, 0)
        self._right_offset = pygame.Vector2(20, 0)

    @property
    def current_image(self):
        return self._sprites[self.direction][self.current_frame_index]

    def sync_with_player(self, player):
        self._direction = player.direction

        if self._direction == Direction.UP or self._direction == Direction.DOWN:
            self._state = State.IDLE
            self.reset_animation()
            return

        if self._direction == Direction.LEFT:
            self._position = player.position + self._left_offset
        elif self._direction == Direction.RIGHT:
            self._position = player.position + self._right_offset

        self._hitbox.move(self._position)

    def attack(self, room, player):
        if self.direction == Direction.UP or self.direction == Direction.DOWN:
            return

        self._state = State.ATTACKING
        self.reset_animation()

        for entity in room.entity_list:
            if entity.entity_id in const.ENEMY_IDS:
                if self.hitbox.is_colliding(entity.hitbox):
                    entity.take_damage(player.stats.damage.damage)

    def stop_attack(self):
        self._state = State.IDLE
        self.reset_animation()

    def update(self):
        if self._state != State.ATTACKING:
            self._state = State.IDLE
            self.reset_animation()
            return

        self.animate(self._sprites[self.direction])

    def render(self, screen):
        if self.direction == Direction.UP or self.direction == Direction.DOWN:
            return

        screen.blit(self.current_image, self.position)