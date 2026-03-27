from scripts.building_blocks.room import Room
from scripts.generators.background_generator import BackgroundGenerator
from scripts.generators.generator import Generator
from scripts.generators.spawner import Spawner
from scripts.managers.collision_manager import CollisionManager


class DungeonGenerator(Generator):
    def __init__(self, player_choice):
        self._spawner = Spawner()
        self._collision_manager = CollisionManager()
        self._background_generator = BackgroundGenerator()
        self._player = self._spawner.spawn_player(player_choice)

    @property
    def player(self):
        return self._player

    def generate_first_room(self):
        background = self._background_generator.generate()
        return Room(background, [], self._player)

    def generate(self):
        spawned_entities = self._spawner.spawn_entities()
        background = self._background_generator.generate()
        return Room(background, spawned_entities, self._collision_manager, None)