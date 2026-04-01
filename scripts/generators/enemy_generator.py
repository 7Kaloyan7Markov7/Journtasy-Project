from random import randint, choice

from scripts.generators.generator import Generator
from scripts.entities.enemy import Enemy
import scripts.config.constants as const


class EnemyGenerator(Generator):
    def generate(self):
        random_id = choice(const.ENEMY_IDS)
        position = (randint(0, const.SCREEN_WIDTH - const.SPAWN_MARGIN), randint(0, const.SCREEN_HEIGHT - const.SPAWN_MARGIN))
        return Enemy(random_id, position, const.SPEED_DATA[const.ENEMY_ID][random_id], randint(1, const.MAX_ENEMY_LEVEL))