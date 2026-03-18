from abc import ABC, abstractmethod

from pygame import Vector2, Rect
from enums import Direction, State

class Entity(ABC):
    def __init__(self, entity_id, position, speed):
        self._entity_id = str(entity_id)
        self._direction = Direction.NO_DIRECTION
        self._state = State.NO_STATE
        self._current_frame_index = 0
        self._sprites = None
        self._position = Vector2(position)
        self._speed = int(speed)
        self._hitbox = None

    @property
    def direction(self):
        return self._direction
    
    @property
    def current_frame_index(self):
        return self._current_frame_index
    
    @property
    def state(self):
        return self._state
    
    @property
    def entity_id(self):
        return self._entity_id
    
    @property
    def hitbox(self):
        return self._hitbox
    
    @property
    def width(self):
        return self.hitbox.width
    
    @property
    def height(self):
        return self.hitbox.height
    
    @property
    def position(self):
        return self._position

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass
