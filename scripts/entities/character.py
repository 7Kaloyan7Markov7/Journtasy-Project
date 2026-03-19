from abc import abstractmethod
from scripts.character_stats.stats import Stats
from scripts.entities.animated_entity import AnimatedEntity


class Character(AnimatedEntity):
    def __init__(self, entity_id, position, speed, level):
        super().__init__(entity_id, position, speed)
        self._stats = Stats(entity_id, level)
        self._sprites = {}
        self._previous_position = self.position.copy()

    @property
    def previous_position(self):
        return self._previous_position

    @property
    def level(self):
        return self._stats.level
    
    @property
    def stats(self):
        return self._stats
    
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
    def attack(self, context=None):
        pass

    @abstractmethod
    def move(self, context=None):
        pass