from scripts.entities.player import Player
from scripts.generators.projectile_generator import ProjectileGenerator
import scripts.config.constants as const


class RangedPlayer(Player):
    def __init__(self, entity_id, position, speed, level):
        super().__init__(entity_id, position, speed, level)
        self._fire_cooldown = 0
        self._fire_delay = const.PLAYER_FIRE_DELAY
        self._projectile_gen = ProjectileGenerator()
        self._projectile_id = const.PLAYER_PROJECTILE_MAP[entity_id]

    def update(self):
        super().update()
        if self._fire_cooldown > 0:
            self._fire_cooldown -= 1

    def attack(self, target=None):
        if target is not None:
            return None

        if self._fire_cooldown > 0:
            return None

        self._fire_cooldown = self._fire_delay
        proj_w = const.PROJECTILE_WIDTH * const.PROJECTILE_SCALE
        proj_h = const.PROJECTILE_HEIGHT * const.PROJECTILE_SCALE
        fire_x = self.position.x + self.width / 2 - proj_w / 2
        fire_y = self.position.y + self.height / 2 - proj_h / 2
        return self._projectile_gen.generate((fire_x, fire_y), self._projectile_id, self.direction, self)

    def render(self, screen):
        screen.blit(self.current_image, self.position)
