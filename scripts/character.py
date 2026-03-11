from entity import Entity


class Character(Entity):
    def __init__(self, entity_id, state, position, velocity, current_frame, hitbox, stats):
        super().__init__(entity_id, state, position, velocity, current_frame, hitbox)
        self.stats = stats
        self.alive = True
    
    def take_damage(self, damage):
        pass

    def attack(self):
        pass

    def move(self):
        pass