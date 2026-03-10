from pygame import Vector2, Rect

class Entity:
    def __init__(self, entity_id, state, position, velocity, current_frame, hitbox):
        self.entity_id = str(entity_id)
        self.state = state
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.current_frame = int(current_frame)
        self.hitbox = hitbox