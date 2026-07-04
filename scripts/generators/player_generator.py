from scripts.generators.generator import Generator
from scripts.entities.melee_player import MeleePlayer
from scripts.entities.ranged_player import RangedPlayer
import scripts.config.constants as const


class PlayerGenerator(Generator):
    def __init__(self, player_choice):
        self._player_choice = player_choice

    def generate(self):
        speed = const.SPEED_DATA[const.PLAYER_ID][self._player_choice]

        if self._player_choice in const.RANGED_PLAYER_IDS:
            return RangedPlayer(self._player_choice, (100, 100), speed, const.FIRST_LEVEL)
        return MeleePlayer(self._player_choice, (100, 100), speed, const.FIRST_LEVEL)
