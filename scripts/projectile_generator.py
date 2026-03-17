from generator import Generator
from projectile import Projectile
from character import Character
import constants as const


class ProjectileGenerator(Generator):
    def __init__(self, sender):
        self._position = sender.position
        self._entity_id = sender.entity_id

    def generate(self):
        speed = const.SPEED_DATA[const.PROJECTILE_ID][self._entity_id]
        return Projectile(self._entity_id, self._position, speed)