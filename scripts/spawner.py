from random import randint

from entity import Entity
from player import Player
from enemy import Enemy
from projectile import Projectile
from weapon import Weapon
from obstacle import Obstacle
from stats import Stats
import constants as const


class Spawner:
    def __init__(self, enemy_generator):
        self.enemy_generator = enemy_generator

    def spawn_player(self):
        ...

    #enemy
    def spawn_enemy(self):
        random_id = const.ENEMY_IDS[randint(0, len(const.ENEMY_IDS) - 1)]
        return self.enemy_generator.generate(random_id)

    def spawn_obstacle(self):
        ...

    def spawn_weapon(self):
        ...

    def spawn_projectile(self):
        ...

    def spawn_entities(self):
        entity_list = []

        return entity_list