from random import randint, getrandbits

from scripts.generators.generator import Generator
from scripts.entities.obstacle import Obstacle
import scripts.config.constants as const

class ObstacleGenerator(Generator):
    def generate(self):
        random_id = const.OBSTACLE_IDS[randint(0, len(const.OBSTACLE_IDS) - 1)]

        position = (randint(200 + const.PLAYER_SPRITE_WIDTH,
                    const.SCREEN_WIDTH - 200 - const.PLAYER_SPRITE_WIDTH),
                    randint(200 + const.PLAYER_SPRITE_HEIGHT,
                    const.SCREEN_HEIGHT - 200 - const.PLAYER_SPRITE_HEIGHT))
        
        return Obstacle(random_id, position, const.ZERO_SPEED)