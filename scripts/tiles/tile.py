from scripts.collisions.hitbox import HitBox

class Tile:
    def __init__(self, position):
        self._hitbox = HitBox(position, 40, 40)
        self._is_blocked = False
        self._tile_left = None
        self._tile_right = None
        self._tile_up = None
        self._tile_down = None

    @property
    def tile_left(self):
        return self._tile_left
    
    @property
    def tile_right(self):
        return self._tile_right
    
    @property
    def tile_up(self):
        return self._tile_up
    
    @property
    def tile_down(self):
        return self._tile_down
    
    @property
    def is_blocked(self):
        return self._is_blocked
    
    @property
    def hitbox(self):
        return self._hitbox
    
    @tile_left.setter
    def tile_left(self, value):
        self._tile_left = value

    @tile_right.setter
    def tile_right(self, value):
        self._tile_right = value

    @tile_down.setter
    def tile_down(self, value):
        self._tile_down = value

    @tile_up.setter
    def tile_up(self, value):
        self._tile_up = value

    @is_blocked.setter
    def is_blocked(self, value):
        self._is_blocked = value