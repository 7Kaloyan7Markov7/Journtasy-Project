from entity import Entity
from abc import abstractmethod


class Character(Entity):
    def __init__(self, entity_id, state, position, velocity, current_frame, hitbox, stats):
        super().__init__(entity_id, state, position, velocity, current_frame, hitbox)
        self.stats = stats
        self.alive = True

    @abstractmethod
    def take_damage(self, damage):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass