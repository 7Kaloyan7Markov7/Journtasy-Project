from random import randint, getrandbits

from scripts.generators.generator import Generator
from scripts.entities.obstacle import Obstacle
import scripts.config.constants as const

class ObstacleGenerator(Generator):
    def generate(self):
        random_id = const.OBSTACLE_IDS[randint(0, len(const.OBSTACLE_IDS) - 1)]
        position = (randint(0, const.SCREEN_WIDTH - 200), randint(0, const.SCREEN_HEIGHT - 200))
        return Obstacle(random_id, position, const.ZERO_SPEED)