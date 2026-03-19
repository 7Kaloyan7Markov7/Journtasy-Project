from abc import abstractmethod

from scripts.character_stats.stats import Stats
from scripts.entities.entity import Entity


class Character(Entity):
    def __init__(self, entity_id, position, speed, level):
        super().__init__(entity_id, position, speed)
        self._stats = Stats(entity_id, level)
        self._sprites = {}
        
    @property
    def level(self):
        return self._stats.level
    
    @level.setter
    def level(self, new_level):
        self._stats.level = new_level

    def update(self):
        self._stats.update()

    def level_up(self):
        self._stats.level_up()

    def take_damage(self, damage):
        self._stats.take_damage(damage)

    @abstractmethod
    def attack(self, context = None):
        pass

    @abstractmethod
    def move(self, context = None):
        pass