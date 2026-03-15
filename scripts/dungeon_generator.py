from asset_manager import AssetManager
from room import Room
from constants import BACKGROUND_IDS
from background import Background
from background_generator import BackgroundGenerator
from generator import Generator


class DungeonGenerator(Generator):
    def __init__(self, spawner, background_generator):
        self.spawner = spawner
        self.background_generator = background_generator

    def generate(self):
        spawned_entities = self.spawner.spawn_entities()
        background = self.background_generator.generate()

        new_room = Room(background, spawned_entities)
        return new_room