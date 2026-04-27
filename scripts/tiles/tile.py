from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import Direction


class Tile:
    def __init__(self, position):
        self._hitbox = HitBox(position, 40, 40)
        self._is_blocked = False

    @property
    def is_blocked(self):
        return self._is_blocked

    @property
    def hitbox(self):
        return self._hitbox

    @is_blocked.setter
    def is_blocked(self, value):
        self._is_blocked = value
