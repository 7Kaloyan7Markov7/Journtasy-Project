import pygame

from scripts.scenes.scene import Scene
from scripts.gui.gui import GUI
import scripts.config.constants as const


class GameScene(Scene):
    scene_id = const.GAME_SCENE_ID

    def __init__(self, room):
        self._room = room
        self._is_paused = False
        self._is_game_over = False
        self._gui = GUI()
        self._font = pygame.font.SysFont(None, const.GAME_FONT_SIZE)

    @property
    def room(self):
        return self._room

    @property
    def is_paused(self):
        return self._is_paused

    @property
    def is_game_over(self):
        return self._is_game_over

    @room.setter
    def room(self, new_room):
        self._room = new_room

    def update(self):
        if self.is_paused or self.is_game_over:
            return

        self._room.update()

    def render(self, screen):
        self._room.render(screen)
        self._gui.render(screen, self._room)

        if self._is_paused:
            text_surface = self._font.render(const.PAUSED_TEXT, True, const.PAUSE_TEXT_COLOR)
            text_rect = text_surface.get_rect(center=screen.get_rect().center)
            screen.blit(text_surface, text_rect)

        if self._is_game_over:
            overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            screen.blit(overlay, (0, 0))
            text_surface = self._font.render(const.GAME_OVER_TEXT, True, const.GAME_OVER_TEXT_COLOR)
            text_rect = text_surface.get_rect(center=screen.get_rect().center)
            screen.blit(text_surface, text_rect)

    def pause(self):
        self._is_paused = not self._is_paused

    def game_over(self):
        self._is_game_over = True
