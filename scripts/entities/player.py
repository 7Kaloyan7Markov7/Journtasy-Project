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
        self._exp_threshhold = 100

        weapon_id = const.PLAYER_WEAPON_MAP[entity_id]
        self._weapon = Weapon(weapon_id, position, speed)
        self._sprites = AssetManager.get_player_animations(entity_id)

        self._invulnerability_timer = 0
        self._invulnerability_duration = 30
        self._just_transitioned = False

        hitbox_data = const.HITBOX_DATA[const.PLAYER_ID]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

    @property
    def weapon(self):
        return self._weapon

    @property
    def just_transitioned(self):
        return self._just_transitioned

    @just_transitioned.setter
    def just_transitioned(self, value):
        self._just_transitioned = value

    @property
    def current_image(self):
        return self._sprites[self.direction][self.current_frame_index]

    def update(self):
        super().update()
        self._level_up()
        self._just_transitioned = False

        if self._invulnerability_timer > 0:
            self._invulnerability_timer -= 1

        if self.state == State.MOVING:
            self.animate()

        self.weapon.sync_with_player(self)
        self.weapon.update()

        if self.weapon.state == State.IDLE and self._state == State.ATTACKING:
            self._state = State.IDLE

    def take_damage(self, damage):
        if self._invulnerability_timer > 0 or self.stats.is_dead:
            return

        self.stats.take_damage(damage)
        self._invulnerability_timer = self._invulnerability_duration

    def attack(self, target=None):
        if target is None:

            # Initiate the swing
            if self.direction == Direction.DOWN or self.direction == Direction.UP:
                return
            if self.weapon.state == State.ATTACKING:
                return
            self.weapon.attack()
            if self.weapon.state == State.ATTACKING:
                self._state = State.ATTACKING
        else:
            # Apply hit to a target
            self.weapon.apply_damage(target, self.stats.damage.damage)
            if target.stats.is_dead:
                self._experience_bar += target.exp_on_kill

    def _level_up(self):
        while self._experience_bar >= self._exp_threshhold:
            self.stats.level_up()
            self._experience_bar -= self._exp_threshhold
            print(f"Leveled up to level {self.stats.level}!")


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
        pygame.draw.rect(screen,(0,0,0), self.hitbox.hitbox)