from abc import abstractmethod

from stats import Stats
from entity import Entity


class Character(Entity):
    def __init__(self, entity_id, position, speed, level):
        super().__init__(entity_id, position, speed)
        self.stats = Stats(entity_id, level)
        self.sprites = {}

    @property
    def level(self):
        return self.stats.level
    
    @level.setter
    def level(self, new_level):
        self.stats.level = new_level

    def update(self):
        self.stats.update()

    def level_up(self):
        self.stats.level_up()

    def take_damage(self, damage):
        self.stats.take_damage(damage)

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass