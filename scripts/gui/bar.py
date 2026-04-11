from abc import ABC, abstractmethod
import pygame


class Bar(ABC):
    def __init__(self, width, height, y_offset, border_color, background_color, fill_color):
        self._width = width
        self._height = height
        self._y_offset = y_offset

        self._border_color = border_color
        self._background_color = background_color
        self._fill_color = fill_color
        

    @abstractmethod
    def update(self, entity):
        raise NotImplementedError

    def render(self, screen):
        pygame.draw.rect(screen, self._background_color, self._background_rect)
        pygame.draw.rect(screen, self._fill_color, self._fill_rect)
        pygame.draw.rect(screen, self._border_color, self._background_rect, 1)
