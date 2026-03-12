import pygame


class Background:
    def  __init__(self, background_id, image):
        self.background_id = background_id
        self.image = image
    
    def render(self, screen):
        screen.blit(self.image, (0, 0))
