from scripts.entities.animated_entity import AnimatedEntity
from scripts.managers.asset_manager import AssetManager
from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import State, Direction
from scripts.managers.sound_manager import SoundManager
import scripts.config.constants as const
import pygame


class Weapon(AnimatedEntity):
    def __init__(self, entity_id, position, speed):
        super().__init__(entity_id, position, speed)
        self._sprites = AssetManager.get_weapon_animations(entity_id)
        self._id = entity_id

        hitbox_data = const.HITBOX_DATA[const.WEAPON_ID][entity_id]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

        self._hit_targets = set()

        self._attack_direction = Direction.RIGHT

    @property
    def current_image(self):
        return self._sprites[self.direction][self.current_frame_index]

    def sync_with_player(self, player):
        player_direction = player.direction

        if player_direction in (Direction.LEFT, Direction.RIGHT):
            self._attack_direction = player_direction

        if self._state == State.ATTACKING:
            self._direction = self._attack_direction
        else:
            self._direction = player_direction

        # hide weapon when idle and player faces up/down
        if self._state != State.ATTACKING and player_direction in (Direction.UP, Direction.DOWN):
            self.reset_animation()
            self._position = player.position.copy()
            self._hitbox.move((const.WEAPON_HIDE_POSITION, const.WEAPON_HIDE_POSITION))
            self._hit_targets.clear()
            return

        left_extra_x, right_extra_x, extra_y = const.WEAPON_OFFSET_DATA.get(self._id, (0, 0, 0))
        vertical_offset = (player.height - self.height) / 2 + extra_y

        if self._direction == Direction.LEFT:
            horizontal_offset = -self.width + left_extra_x
        else:
            horizontal_offset = player.width - right_extra_x

        self._position = player.position + pygame.Vector2(horizontal_offset, vertical_offset)

        self._hitbox.move(self._position)

    def attack(self):
        if self._state == State.ATTACKING:
            return
        


        SoundManager.play_sound(self._id)

        self._state = State.ATTACKING
        self._direction = self._attack_direction
        self.reset_animation()
        self._hit_targets.clear()

    def apply_damage(self, target, damage):
        if self._state != State.ATTACKING or target in self._hit_targets:
            return False

        target.take_damage(damage)
        self._hit_targets.add(target)
        return True

    def stop_attack(self):
        self._state = State.IDLE
        self.reset_animation()
        self._hit_targets.clear()

    def update(self):
        if self._state != State.ATTACKING:
            self._state = State.IDLE
            self.reset_animation()
            return

        frame_count = len(self._sprites[self.direction])

        if self._current_frame_index >= frame_count - 1:
            self.stop_attack()
            return

        self.animate()

    def render(self, screen):
        if self._state != State.ATTACKING and self.direction in (Direction.UP, Direction.DOWN):
            return

        screen.blit(self.current_image, self.position)