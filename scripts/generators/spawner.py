from random import randint

from enemy_generator import EnemyGenerator
from scripts.generators.player_generator import PlayerGenerator
from scripts.generators.obstacle_generator import ObstacleGenerator
import scripts.config.constants as const


class Spawner:
    def __init__(self):
        self._enemy_generator = EnemyGenerator()
        self._obstacle_generator = ObstacleGenerator()

    #spawns player by choice
    def spawn_player(self, choice):
        player_generator = PlayerGenerator(choice)
        return player_generator.generate()

    #spawns random enemy
    def spawn_enemy(self):
        return self._enemy_generator.generate()

    #spawns random obstacle
    def spawn_obstacle(self):
        return self._obstacle_generator.generate()
    
    def spawn_entities(self):
        entity_list = []

        count_of_enemies = randint(1,5)
        iter = 0
        while(iter < count_of_enemies):
            entity_list.append(self.spawn_enemy())
            iter += 1

        count_of_obstacles = randint(1,5)
        iter = 0
        while(iter < count_of_obstacles):
            entity_list.append(self.spawn_obstacle())
            iter += 1

        return entity_list