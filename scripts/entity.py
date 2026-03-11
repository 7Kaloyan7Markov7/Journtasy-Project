from pygame import Vector2, Rect
from enums import Direction, State
from abc import ABC
from abc import abstractmethod
from asset_manager import AssetManager


class Entity(ABC):
    def __init__(self, entity_id, position, velocity, hitbox):
        self.direction = Direction.NO_DIRECTION
        self.state = State.NO_STATE
        self.current_frame_index = 0
        self.sprites = {}
        self.entity_id = str(entity_id)
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.hitbox = Rect(hitbox)

    @abstractmethod
    def update(self):
        pass
    
    def load(self):
        self.sprites = AssetManager.load_animations(self.entity_id)
