from abc import abstractmethod

from entity import Entity


class Character(Entity):
    def __init__(self, entity_id, position, velocity, hitbox, stats):
        super().__init__(entity_id, position, velocity, hitbox)
        self.stats = stats
        self.alive = True
        self.sprites = {}

    @abstractmethod
    def kill_character(self):
        ...

    @abstractmethod
    def take_damage(self, damage):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass