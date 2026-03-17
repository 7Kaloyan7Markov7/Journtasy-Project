from asset_manager import AssetManager
from room import Room
from constants import BACKGROUND_IDS
from background_generator import BackgroundGenerator
from generator import Generator
from spawner import Spawner


class DungeonGenerator(Generator):
    def __init__(self):
        self.spawner = Spawner()
        self.background_generator = BackgroundGenerator()

    def generate(self):
        spawned_entities = self.spawner.spawn_entities()
        background = self.background_generator.generate()

        new_room = Room(background, spawned_entities)
        return new_room