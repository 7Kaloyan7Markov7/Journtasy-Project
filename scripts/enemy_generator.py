from random import randint

from generator import Generator
from enemy import Enemy
import constants as const

class EnemyGenerator(Generator):
    def generate(self):
        random_id = const.ENEMY_IDS[randint(0, len(const.ENEMY_IDS) - 1)]
        position = (randint(0, const.SCREEN_WIDTH), randint(0, const.SCREEN_HEIGHT))
        return Enemy(random_id, position, const.SPEED_DATA[const.ENEMY_ID][random_id])