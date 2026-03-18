import pygame

from scripts.managers.asset_manager import AssetManager
from scripts.managers.scene_manager import SceneManager
from scripts.managers.input_manager import InputManager
from scripts.managers.event_handler_manager import EventHandlerManager
import scripts.config.constants as const


class Game:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()
        self._running = True
        self._scene_manager = SceneManager()
        self._input_manager = InputManager()
        self._event_handler_manager = EventHandlerManager()

    @property
    def scene_manager(self):
        return self._scene_manager
    
    @property
    def input_manager(self):
        return self._scene_manager
    
    @property
    def running(self):
        return self._running
    
    @running.setter
    def running(self, running):
        self._running = running

    def main_loop(self):

        self.load_game()
        while self.running:
            self.update_game()
            self.render_game()
            self.clock.tick(const.SIXTY_FPS)

        pygame.quit()

    def load_game(self):
        AssetManager.load()    

    def update_game(self):
        self._input_manager.update()
        self._event_handler_manager.handle(self)
        self._scene_manager.update_scene()

    def render_game(self):
        self._scene_manager.render_scene(self.screen)
        pygame.display.flip()