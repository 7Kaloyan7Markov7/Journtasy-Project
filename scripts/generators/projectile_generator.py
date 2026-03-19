from scripts.generators.generator import Generator
from scripts.entities.projectile import Projectile
from scripts.entities.character import Character
import scripts.config.constants as const


#enemies that fire projectiles will have ProjectileGenerator as attribute
class ProjectileGenerator(Generator):
        def generate(self, position, entity_id, direction, owner):
            speed = const.SPEED_DATA[const.PROJECTILE_ID][entity_id]

            return Projectile(entity_id, position, speed, direction, owner)