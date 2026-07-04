from scripts.entities.entity import Entity
from scripts.managers.asset_manager import AssetManager
from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import Direction
import scripts.config.constants as const


class Projectile(Entity):
    def __init__(self, entity_id, position, speed, direction, owner):
        super().__init__(entity_id, position, speed)
        self._sprites = AssetManager.get_projectile_animations(entity_id)
        self._direction = direction
        self._owner = owner
        self._current_frame_index = 0

        hitbox_data = const.HITBOX_DATA[const.PROJECTILE_ID][entity_id]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

    @property
    def current_image(self):
        return self._sprites[self.direction][self._current_frame_index]

    @property
    def owner(self):
        return self._owner

    @property
    def damage(self):
        return self._owner.stats.damage.damage

    def update(self):
        if self.direction == Direction.LEFT:
            self._position.x -= self.speed
        elif self.direction == Direction.RIGHT:
            self._position.x += self.speed
        elif self.direction == Direction.UP:
            self._position.y -= self.speed
        elif self.direction == Direction.DOWN:
            self._position.y += self.speed

        self._hitbox.move(self._position)

        frame_count = len(self._sprites[self._direction])
        self._current_frame_index = (self._current_frame_index + 1) % frame_count

    def render(self, screen):
        screen.blit(self.current_image, self.position)
