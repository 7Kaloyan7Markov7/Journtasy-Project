import pygame

from scripts.scenes.scene import Scene
import scripts.config.constants as const


class GameScene(Scene):
    scene_id = const.GAME_SCENE_ID

    def __init__(self, room):
        self._room = room
        self._is_paused = False
        self._font = pygame.font.SysFont(None, 64)

    @property
    def room(self):
        return self._room
    
    @property
    def is_paused(self):
        return self._is_paused
    
    @room.setter
    def room(self, new_room):
        self._room = new_room

    def update(self):
        if not self.is_paused:
            self._room.update()

    def render(self, screen):
        self._room.render(screen)
        if self._is_paused:
            text_surface = self._font.render(const.PAUSED_TEXT, True, (0, 255, 0))
            text_rect = text_surface.get_rect(center=screen.get_rect().center)
            screen.blit(text_surface, text_rect)

    def pause(self):
        self._is_paused = not self._is_paused