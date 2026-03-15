from random import randint

from entity import Entity
from player import Player
from enemy import Enemy
from projectile import Projectile
from weapon import Weapon


class Spawner:
    def spawn_player(self):
        ...

    #enemy
    def spawn_enemy(self):
        ...

    def spawn_obstacle(self):
        ...

    def spawn_weapon(self):
        ...

    def spawn_projectile(self):
        ...

    def spawn_entities(self):
        entity_list = []

        return entity_list