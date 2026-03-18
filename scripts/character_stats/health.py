import scripts.config.constants as const
from stat import Stat


class Health(Stat):
    def __init__(self, entity_id, level):
        self._base_health = const.CHARACTER_STATS[entity_id][const.HEALTH][0]
        self._health_growth = const.CHARACTER_STATS[entity_id][const.HEALTH][1]
        self._healing = const.CHARACTER_STATS[entity_id][const.HEALTH][2]
        self._max_health = self._base_health + self._health_growth * (level - 1)
        self._current_health = self._max_health

    @property
    def current_health(self):
        return self._current_health

    @property
    def max_health(self):
        return self._max_health

    @current_health.setter
    def current_health(self, new_health):
        self._current_health = new_health

    @max_health.setter
    def max_health(self, new_max_health):
        self._max_health = new_max_health

    def increase(self, level):
        self.max_health = self._base_health + self._health_growth * (level - 1)
    
    def update(self):
        self.current_health = min(self.max_health, self.current_health + self._healing)

    def take_damage(self, damage):
        self.current_health = max(0, self.current_health - damage)