from dungeon_generator import DungeonGenerator
import constants as const

class DungeonManager:
    def __init__(self, player_choice):
        self._generated_rooms = {}
        self._room_count = 0
        self._dungeon_generator = DungeonGenerator(player_choice)
        self._current_room = self._dungeon_generator.generate_first_room()
        self.player_choice = player_choice
        self._has_dungeon_started = False

    @property
    def has_dungeon_started(self):
        return self._has_dungeon_started

    @property
    def room_count(self):
        return self._room_count
    
    @property
    def current_room(self):
        return self._current_room
    
    @property
    def generated_rooms(self):
        return self._generated_rooms
    
    def move_player_to_room(self, new_room):
        for entity in self.current_room.entity_list:
            if entity.entity_id == self.player_choice:
                taken_player = entity 
                break

        self.current_room.entity_list.remove(taken_player)
        new_room.entity_list.append(taken_player)

    def create_new_room(self):
       new_room = self._dungeon_generator.generate()
       self._generated_rooms[self.room_count] = new_room
       self._room_count += 1
    
    def change_room(self, new_room):
        self.move_player_to_room(new_room)
        self._current_room = new_room

    def start_dungeon(self):
        self._has_dungeon_started = True
        self._generated_rooms.generate_first_room(self.player_choice)  