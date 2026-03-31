from abc import ABC, abstractmethod
from pygame import Vector2
from scripts.enums.enums import Direction, State


class Entity(ABC):
    def __init__(self, entity_id, position, speed):
        self._entity_id = str(entity_id)
        self._direction = Direction.DOWN
        self._state = State.IDLE
        self._position = Vector2(position)
        self._speed = int(speed)
        self._hitbox = None

    @property
    def direction(self):
        return self._direction
    
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
    
    @position.setter
    def position(self, new_position):
        self._position = new_position
    
    @property
    def speed(self):
        return self._speed
    
    @state.setter
    def state(self, new_state):
        self._state = new_state

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass