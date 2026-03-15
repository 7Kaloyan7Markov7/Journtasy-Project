from pygame import Vector2, Rect
from enums import Direction, State
from abc import ABC, abstractmethod
from asset_manager import AssetManager


class Entity(ABC):
    def __init__(self, entity_id, position, velocity, hitbox):
        self.entity_id = str(entity_id)
        self.direction = Direction.NO_DIRECTION
        self.state = State.NO_STATE
        self.current_frame_index = 0
        self.sprites = None
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.hitbox = Rect(hitbox)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    
