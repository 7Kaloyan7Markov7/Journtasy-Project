from stat import Stat
import scripts.config.constants as const


class Armor(Stat):
    def __init__(self, entity_id, level):
        self._base_armor = const.CHARACTER_STATS[entity_id][const.ARMOR][0]
        self._armor_growth = const.CHARACTER_STATS[entity_id][const.ARMOR][1]
        self._armor = self._base_armor + self._armor_growth * (level - 1)

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, new_armor):
        self._armor = new_armor

    def increase(self, level):
        self.armor = self._base_armor + self._armor_growth * (level - 1)

    def reduce_damage(self, damage):
        return max(0, damage - self.armor)