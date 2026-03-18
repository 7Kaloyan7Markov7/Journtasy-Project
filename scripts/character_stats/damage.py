from stat import Stat
import scripts.config.constants as const


class Damage(Stat):
    def __init__(self, entity_id, level):
        self._base_damage = const.CHARACTER_STATS[entity_id][const.DAMAGE][0]
        self._damage_growth = const.CHARACTER_STATS[entity_id][const.DAMAGE][1]
        self._damage = self._base_damage + self._damage_growth * (level - 1)

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, new_damage):
        self._damage = new_damage

    def increase(self, level):
        self.damage = self._base_damage + self._damage_growth * (level - 1)