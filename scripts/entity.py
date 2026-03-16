from abc import ABC, abstractmethod

from pygame import Vector2, Rect
from enums import Direction, State

class Entity(ABC):
    def __init__(self, entity_id, position, speed):
        self.entity_id = str(entity_id)
        self.direction = Direction.NO_DIRECTION
        self.state = State.NO_STATE
        self.current_frame_index = 0
        self.sprites = None
        self.position = Vector2(position)
        self.speed = int(speed)
        self.hitbox = None

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass
