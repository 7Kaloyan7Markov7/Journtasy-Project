class DungeonManager:
    def __init__(self, dungeon_generator):
        self.generated_rooms = {}
        self.room_count = 0
        self.current_room = None
        self.dungeon_generator = dungeon_generator

    def create_room(self):
       new_room = self.dungeon_generator.generate_room()
       self.generated_rooms[self.room_count] = new_room
       room_count += 1
    
    def change_room(self, new_room):
        self.current_room = new_room

    @property
    def get_current_room(self):
        return self.current_room

    
