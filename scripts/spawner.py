from random import randint

from entity import Entity
from player import Player
from enemy import Enemy
from projectile import Projectile
from weapon import Weapon
from obstacle import Obstacle
from stats import Stats
from enemy_generator import EnemyGenerator
from player_generator import PlayerGenerator
import constants as const


class Spawner:
    def __init__(self):
        self._enemy_generator = EnemyGenerator()
        self._obstacle_generator = None
        self._projectile_generator = None
        self._weapon_generator = None

    def spawn_player(self, choice):
        player_generator = PlayerGenerator(choice)
        return player_generator.generate()

    def spawn_enemy(self):
        return self._enemy_generator.generate()

    def spawn_obstacle(self):
        ...

    def spawn_projectile(self):
        ...

    def spawn_entities(self):
        entity_list = []

        return entity_list