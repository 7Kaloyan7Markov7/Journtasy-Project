class Room:
    def __init__(self, background, entity_list, collision_manager, player=None):
        self._background = background
        self._entity_list = entity_list
        self._player = player
        self._collision_manager = collision_manager
        self._left_room = None
        self._right_room = None
        self._up_room = None
        self._down_room = None

    @property
    def player(self):
        return self._player
    
    @property
    def left_room(self):
        return self._left_room

    @left_room.setter
    def left_room(self, new_room):
        self._left_room = new_room

    @property
    def right_room(self):
        return self._right_room

    @right_room.setter
    def right_room(self, new_room):
        self._right_room = new_room

    @property
    def up_room(self):
        return self._up_room

    @up_room.setter
    def up_room(self, new_room):
        self._up_room = new_room

    @property
    def down_room(self):
        return self._down_room

    @down_room.setter
    def down_room(self, new_room):
        self._down_room = new_room

    @player.setter
    def player(self, new_player):
        self._player = new_player

    @property
    def entity_list(self):
        return self._entity_list
    
    @property
    def collision_manager(self):
        return self._collision_manager
    
    def render(self, screen):
        self._background.render(screen)

        if self.player is not None:
            self.player.render(screen)

        for entity in self.entity_list:
            entity.render(screen)

    def update(self):
        if self.player is not None:
            self.player.update()

        for entity in self.entity_list:
            entity.update()