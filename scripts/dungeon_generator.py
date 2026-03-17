from asset_manager import AssetManager
from room import Room
from constants import BACKGROUND_IDS
from background_generator import BackgroundGenerator
from generator import Generator
from spawner import Spawner


class DungeonGenerator(Generator):
    def __init__(self):
        self._spawner = Spawner()
        self._background_generator = BackgroundGenerator()

    @property
    def spawner(self):
        return self._spawner
    
    def generate_first_room(self, player_choice):
        spawned_player = [self.spawner.spawn_player(player_choice)]
        background = self.background_generator.generate()

        first_room = Room(background, spawned_player)
        return first_room

    def generate(self):
        spawned_entities = self.spawner.spawn_entities()
        background = self.background_generator.generate()

        new_room = Room(background, spawned_entities)
        return new_room