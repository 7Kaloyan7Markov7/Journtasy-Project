from dungeon_generator import DungeonGenerator
from enums import Direction
import constants as const


class DungeonManager:
    def __init__(self, player_choice):
        self._dungeon_generator = DungeonGenerator(player_choice)
        self._current_room = self._dungeon_generator.generate_first_room()
        self._player = self._dungeon_generator.spawned_player
        self._has_dungeon_started = False

    @property
    def has_dungeon_started(self):
        return self._has_dungeon_started

    @property
    def current_room(self):
        return self._current_room
    
    def move_player_to_room(self, new_room):
        old_room = self.current_room
        old_room.player = None
        new_room.player = self._player

    def create_new_room(self):
        new_room = self._dungeon_generator.generate()
        return new_room
    
    def transition_to_new_room(self, direction):
        current = self.current_room

        if direction == Direction.RIGHT:
            if current.right_room is None:
                new_room = self.create_new_room()
                current.right_room = new_room
                new_room.left_room = current
            else:
                new_room = current.right_room

        elif direction == Direction.LEFT:
            if current.left_room is None:
                new_room = self.create_new_room()
                current.left_room = new_room
                new_room.right_room = current
            else:
                new_room = current.left_room

        elif direction == Direction.UP:
            if current.up_room is None:
                new_room = self.create_new_room()
                current.up_room = new_room
                new_room.down_room = current
            else:
                new_room = current.up_room

        elif direction == Direction.DOWN:
            if current.down_room is None:
                new_room = self.create_new_room()
                current.down_room = new_room
                new_room.up_room = current
            else:
                new_room = current.down_room

        self.move_player_to_room(new_room)
        self._current_room = new_room

    def start_dungeon(self):
        self._has_dungeon_started = True