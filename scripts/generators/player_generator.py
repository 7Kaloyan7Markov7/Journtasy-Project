from scripts.generators.generator import Generator
from scripts.entities.player import Player
import scripts.config.constants as const


class PlayerGenerator(Generator):
    def __init__(self, player_choice):
        self._player_choice = player_choice

    def generate(self):
        speed = const.SPEED_DATA[const.PLAYER_ID][self._player_choice]

        return Player(self._player_choice, (100, 100), speed, const.FIRST_LEVEL)