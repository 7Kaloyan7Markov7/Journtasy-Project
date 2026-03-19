from scripts.entities.animated_entity import AnimatedEntity
from scripts.managers.asset_manager import AssetManager
from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import Direction
import scripts.config.constants as const


class Projectile(AnimatedEntity):
    def __init__(self, entity_id, position, speed, direction, owner):
        super().__init__(entity_id, position, speed)
        self._sprites = AssetManager.get_projectile_animations(entity_id)
        self._direction = direction
        self._owner = owner

        hitbox_data = const.HITBOX_DATA[const.PROJECTILE_ID][entity_id]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

    @property
    def current_image(self):
        return self._sprites[self.direction][self.current_frame_index]

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
        self.animate(self._sprites[self.direction])

    def render(self, screen):
        screen.blit(self.current_image, self.position)