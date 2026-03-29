from random import randint, choice

from scripts.generators.generator import Generator
from scripts.entities.enemy import Enemy
import scripts.config.constants as const


class EnemyGenerator(Generator):
    def generate(self):
        random_id = choice(const.ENEMY_IDS)
        position = (randint(0, const.SCREEN_WIDTH - 200), randint(0, const.SCREEN_HEIGHT - 200))
        return Enemy(random_id, position, const.SPEED_DATA[const.ENEMY_ID][random_id], randint(1, 3))