from scripts.entities.character import Character
from scripts.managers.asset_manager import AssetManager
from scripts.entities.weapon import Weapon
from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import Direction, State
import math
import scripts.config.constants as const


class Player(Character):
    def __init__(self, entity_id, position, speed, level):
        super().__init__(entity_id, position, speed, level)
        self._experience = 0

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
        self.weapon.update()

    def render(self, screen):
        screen.blit(self.current_image, self.position)
        self.weapon.render(screen, self.direction)

    def attack(self, context=None):
        room = context
        self._state = State.ATTACKING
        self._weapon.attack(room, self)

    def move(self, context=None):
        input_manager = context
        if input_manager is None:
            return

        dx = 0
        dy = 0

        if input_manager.move_left:
            dx -= 1
            self._direction = Direction.LEFT

        if input_manager.move_right:
            dx += 1
            self._direction = Direction.RIGHT

        if input_manager.move_up:
            dy -= 1
            self._direction = Direction.UP

        if input_manager.move_down:
            dy += 1
            self._direction = Direction.DOWN

        if dx == 0 and dy == 0:
            return

        self._previous_position = self.position.copy()

        length = math.sqrt(dx * dx + dy * dy)
        dx = (dx / length) * self.speed
        dy = (dy / length) * self.speed

        self._position.x += dx
        self._position.y += dy
        self.hitbox.move(self.position)