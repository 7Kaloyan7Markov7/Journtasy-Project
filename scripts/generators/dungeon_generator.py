from scripts.managers.asset_manager import AssetManager
from scripts.building_blocks.room import Room
from scripts.generators.background_generator import BackgroundGenerator
from scripts.generators.generator import Generator
from scripts.generators.spawner import Spawner


class DungeonGenerator(Generator):
    def __init__(self, player_choice):
        self._spawner = Spawner()
        self._background_generator = BackgroundGenerator()
        self._player = self.spawner.spawn_player(player_choice)

    @property
    def player(self):
        return self._player

    def generate_first_room(self):
        background = self.background_generator.generate()
        return Room(background, [], self.spawned_player)

    def generate(self):
        spawned_entities = self.spawner.spawn_entities()
        background = self.background_generator.generate()
        return Room(background, spawned_entities, None)