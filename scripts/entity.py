from pygame import Vector2, Rect

class Entity:
    def __init__(self, entity_id, state, position, velocity, current_frame_index, hitbox, sprites, direction):
        self.direction = direction
        self.sprites = sprites
        self.entity_id = str(entity_id)
        self.state = state
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.current_frame_index = int(current_frame_index)
        self.hitbox = Rect(hitbox)

    def update():
        pass

    def load_assets():
        pass

    def render():
        pass