from random import randint, choice

from scripts.generators.generator import Generator
from scripts.entities.obstacle import Obstacle
import scripts.config.constants as const


class ObstacleGenerator(Generator):
    def generate(self):
        random_id = choice(const.OBSTACLE_IDS)
        position = (
            randint(const.SPAWN_MARGIN + const.PLAYER_SPRITE_WIDTH, const.SCREEN_WIDTH - const.SPAWN_MARGIN - const.PLAYER_SPRITE_WIDTH),
            randint(const.SPAWN_MARGIN + const.PLAYER_SPRITE_HEIGHT, const.SCREEN_HEIGHT - const.SPAWN_MARGIN - const.PLAYER_SPRITE_HEIGHT),
        )
        return Obstacle(random_id, position, const.ZERO_SPEED)
