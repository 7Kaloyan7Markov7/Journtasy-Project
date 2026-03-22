from scripts.character_stats.armor import Armor
from scripts.character_stats.health import Health
from scripts.character_stats.damage import Damage


class Stats:
    def __init__(self, entity_id, level):
        self._level = int(level)
        self._health = Health(entity_id, level)
        self._armor = Armor(entity_id, level)
        self._damage = Damage(entity_id, level)

    @property
    def health(self):
        return self._health

    @property
    def armor(self):
        return self._armor

    @property
    def damage(self):
        return self._damage

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        self._level = new_level

    @property
    def is_dead(self):
        return self._health.current_health <= 0

    def take_damage(self, damage):
        reduced_damage = max(0, self._armor.reduce_damage(damage))
        self._health.take_damage(reduced_damage)

    def increase_stats(self):
        self._health.increase(self.level)
        self._armor.increase(self.level)
        self._damage.increase(self.level)

    def level_up(self):
        self.level += 1
        self.increase_stats()

    def update(self):
        self.health.update()