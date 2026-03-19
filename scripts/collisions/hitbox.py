import pygame


class HitBox:
    def __init__(self, position, width, height):
        self._width = width
        self._height = height
        self._position = position
        self._hitbox = pygame.Rect(position, (width, height))

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def position(self):
        return self._position

    @property
    def hitbox(self):
        return self._hitbox
    
    @hitbox.setter
    def hitbox(self, other_hitbox):
        self._hitbox = other_hitbox

    def move(self, new_position):
        self._position = new_position
        self._hitbox.topleft = new_position

    def is_colliding(self, other_hitbox):
        return self.hitbox.colliderect(other_hitbox.hitbox)