from scripts.character_stats.armor import Armor
from scripts.character_stats.health import Health
from scripts.character_stats.damage import Damage


class Stats:
    def __init__(self, entity_id, level):
        self._level = int(level)
        self.health = Health(entity_id, level)
        self.armor = Armor(entity_id, level)
        self.damage = Damage(entity_id, level)

    @property
    def level(self):
        return self._level   
    
    @level.setter
    def level(self, new_level):
        self._level = new_level

    def take_damage(self, damage):
        reduced_damage = self.armor.reduce_damage(damage)
        self.health.take_damage(reduced_damage)

    def increase_stats(self):
        self.health.increase(self.level)
        self.armor.increase(self.level)
        self.damage.increase(self.level)

    def level_up(self):
        self.level += 1
        self.increase_stats()

    def is_dead(self):
        return self.health.current_health <= 0
    
    def update(self):
        self.health.update()