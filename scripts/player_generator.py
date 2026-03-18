from generator import Generator
from player import Player
import constants as const


class PlayerGenerator(Generator):
    def __init__(self, player_choice):
        self._player_choice = player_choice

    def generate(self):
        chosen_character_id = const.PLAYABLE_CHARACTER_IDS[self._player_choice]
        speed = const.SPEED_DATA[const.PLAYER_ID][chosen_character_id]

        return Player(chosen_character_id, (100, 100), speed, const.FIRST_LEVEL)