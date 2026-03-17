from random import randint

from enemy_generator import EnemyGenerator
from player_generator import PlayerGenerator
from obstacle_generator import ObstacleGenerator
from projectile_generator import ProjectileGenerator
import constants as const


class Spawner:
    def __init__(self):
        self._enemy_generator = EnemyGenerator()
        self._obstacle_generator = ObstacleGenerator()

    def spawn_player(self, choice):
        player_generator = PlayerGenerator(choice)
        return player_generator.generate()

    def spawn_enemy(self):
        return self._enemy_generator.generate()

    def spawn_obstacle(self):
        return self._obstacle_generator.generate()
    
    def spawn_projectile(self, sender):
        projectile_generator = ProjectileGenerator(sender)
        return projectile_generator.generate()

    def spawn_entities(self):
        entity_list = []

        return entity_list