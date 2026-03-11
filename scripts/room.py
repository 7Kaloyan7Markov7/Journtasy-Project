import pygame


class Room:
    def __init__(self, background, entity_list):
        self.background = background
        self.entity_list = entity_list

    def render(self, screen):
        screen.blit(self.background, (0,0))
        
        for entity in self.entity_list:
            entity.render()

    def update(self):
        for entity in self.entity_list:
            entity.update()