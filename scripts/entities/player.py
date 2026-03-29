from scripts.entities.character import Character
from scripts.managers.asset_manager import AssetManager
from scripts.entities.weapon import Weapon
from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import Direction, State
import scripts.config.constants as const
import pygame

class Player(Character):
    def __init__(self, entity_id, position, speed, level):
        super().__init__(entity_id, position, speed, level)
        self._experience_bar = 0

        weapon_id = const.PLAYER_WEAPON_MAP[entity_id]
        self._weapon = Weapon(weapon_id, position, speed)
        self._sprites = AssetManager.get_player_animations(entity_id)

        hitbox_data = const.HITBOX_DATA[const.PLAYER_ID]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

    @property
    def weapon(self):
        return self._weapon

    @property
    def current_image(self):
        return self._sprites[self.direction][self.current_frame_index]

    def update(self):
        super().update()
        if self.state == State.MOVING:
            self.animate()
        self.weapon.sync_with_player(self)
        self.weapon.update()

        if self.weapon.state == State.IDLE and self._state == State.ATTACKING:
            self._state = State.IDLE

    def attack(self, target=None):
        if self.weapon.state == State.ATTACKING:
            return

        self.weapon.attack()

        if self.weapon.state == State.ATTACKING:
            self._state = State.ATTACKING

    def stop_attack(self):
        self.weapon.stop_attack()

        if self._state == State.ATTACKING:
            self._state = State.IDLE

    def move_left(self):
        self._state = State.MOVING
        self._direction = Direction.LEFT
        self._position.x -= self.speed
        self.hitbox.move(self.position)
        super().animate()

    def move_right(self):
        self._state = State.MOVING
        self._direction = Direction.RIGHT
        self._position.x += self.speed
        self.hitbox.move(self.position)
        super().animate()

    def move_up(self):
        self._state = State.MOVING
        self._direction = Direction.UP
        self._position.y -= self.speed
        self.hitbox.move(self.position)
        super().animate()

    def move_down(self):
        self._state = State.MOVING
        self._direction = Direction.DOWN
        self._position.y += self.speed
        self.hitbox.move(self.position)
        super().animate()

    def render(self, screen):
        screen.blit(self.current_image, self.position)
        self._weapon.render(screen)